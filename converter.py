"""
converter.py  –  Convert a GitHub Copilot chat export (JSON) to one or more
human-readable formats: Markdown, HTML, and/or LaTeX.

Usage:
    python converter.py <chat_file.json> [--format md|html|latex|all]

If --format is omitted, all three formats are produced.

Output files are placed next to the input file:
    chat_summary.md
    chat_summary.html
    chat_summary.tex

What is extracted
-----------------
• Each user message
• Each text response from GitHub Copilot (including "thinking" blocks)
• Tool invocations (name + invocation message)
• Tool results (success and error output)
"""

import json
import sys
import os
import re
import argparse
import html as html_module
from pathlib import Path
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert a Copilot chat JSON export to MD / HTML / LaTeX."
    )
    parser.add_argument("chat_file", help="Path to the chat.json export file")
    parser.add_argument(
        "--format",
        choices=["md", "html", "latex", "all"],
        default="all",
        help="Output format (default: all)",
    )
    return parser.parse_args()


def load_chat(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def timestamp_to_utc(ms) -> str:  # ms: int | None
    if ms is None:
        return ""
    try:
        return datetime.fromtimestamp(ms / 1000.0, tz=timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        )
    except Exception:
        return str(ms)


# ---------------------------------------------------------------------------
# Chat-document model
# ---------------------------------------------------------------------------
# We convert the raw JSON into a flat list of "blocks" that each format can
# render independently.
#
# Block types:
#   ("user",    {"text": ..., "timestamp": ..., "model": ...})
#   ("think",   {"text": ..., "title": ...})
#   ("response",{"text": ...})
#   ("tool",    {"name": ..., "message": ..., "result": ..., "success": bool})
#   ("hr",      {})    – horizontal separator between requests

def build_document(chat_data: dict) -> list:
    """Return a list of (kind, data) blocks."""
    blocks = []
    requests = chat_data.get("requests", [])

    for req_idx, req in enumerate(requests):
        if req_idx > 0:
            blocks.append(("hr", {}))

        # --- User message ---
        msg_text = req.get("message", {}).get("text", "")
        ts = timestamp_to_utc(req.get("timestamp"))
        model = req.get("modelId", "")
        blocks.append(("user", {"text": msg_text, "timestamp": ts, "model": model}))

        # --- Response items ---
        for item in req.get("response", []):
            if not isinstance(item, dict):
                continue
            kind = item.get("kind", "")

            # Plain text response
            if "value" in item and kind not in (
                "thinking", "toolInvocationSerialized",
                "mcpServersStarting", "progressTaskSerialized",
                "confirmation",
            ):
                text = item.get("value", "").strip()
                if text:
                    blocks.append(("response", {"text": text}))

            # Thinking block
            elif kind == "thinking":
                raw_val = item.get("value", "")
                if isinstance(raw_val, list):
                    think_text = "\n".join(str(v) for v in raw_val).strip()
                else:
                    think_text = str(raw_val).strip()
                title = item.get("generatedTitle", "")
                if think_text:
                    blocks.append(("think", {"text": think_text, "title": title}))

            # Tool invocation
            elif kind == "toolInvocationSerialized":
                tool_name = item.get("toolId", "")
                def _msg_value(v):
                    if isinstance(v, dict):
                        return v.get("value", "")
                    if isinstance(v, str):
                        return v
                    return ""
                inv_msg = (
                    _msg_value(item.get("invocationMessage"))
                    or _msg_value(item.get("pastTenseMessage"))
                )
                result_details = item.get("resultDetails", {})
                if not isinstance(result_details, dict):
                    result_details = {}
                result_text = ""
                for out in result_details.get("output", []):
                    if isinstance(out, dict) and isinstance(out.get("value"), str):
                        result_text += out["value"] + "\n"
                result_text = result_text.strip()
                is_error = result_details.get("isError", False)
                blocks.append(
                    (
                        "tool",
                        {
                            "name": tool_name,
                            "message": inv_msg,
                            "result": result_text,
                            "success": not is_error,
                        },
                    )
                )

        # Also extract tool calls recorded in result.metadata.toolCallRounds
        meta = req.get("result", {}).get("metadata", {})
        for rnd in meta.get("toolCallRounds", []):
            rnd_response = rnd.get("response", "").strip()
            if rnd_response:
                blocks.append(("response", {"text": rnd_response}))
            tc_results = rnd.get("toolCallResults", {})
            for tc in rnd.get("toolCalls", []):
                tc_id = tc.get("id", "")
                tc_name = tc.get("name", "")
                inv_msg = f"Calling `{tc_name}`"
                result_text = ""
                is_error = False
                entry = tc_results.get(tc_id)
                if entry:
                    for c in entry.get("content", []):
                        if isinstance(c, dict) and isinstance(c.get("value"), str):
                            result_text += c["value"] + "\n"
                    result_text = result_text.strip()
                    is_error = result_text.startswith("ERROR")
                blocks.append(
                    (
                        "tool",
                        {
                            "name": tc_name,
                            "message": inv_msg,
                            "result": result_text,
                            "success": not is_error,
                        },
                    )
                )

    return blocks


# ---------------------------------------------------------------------------
# Markdown renderer
# ---------------------------------------------------------------------------

def render_markdown(blocks: list) -> str:
    lines = ["# Chat Summary\n"]
    for kind, data in blocks:
        if kind == "hr":
            lines.append("\n---\n")
        elif kind == "user":
            ts = f"  *{data['timestamp']}*" if data["timestamp"] else ""
            model = f"  `{data['model']}`" if data["model"] else ""
            lines.append(f"## 👤 User Request{ts}{model}\n")
            lines.append(data["text"])
            lines.append("")
        elif kind == "response":
            lines.append("**GitHub Copilot:**\n")
            lines.append(data["text"])
            lines.append("")
        elif kind == "think":
            title = data.get("title", "Thinking")
            lines.append(f"<details>\n<summary>🤔 {title or 'Thinking'}</summary>\n")
            lines.append(data["text"])
            lines.append("</details>\n")
        elif kind == "tool":
            icon = "✅" if data["success"] else "❌"
            lines.append(f"**{icon} Tool: `{data['name']}`**\n")
            if data["message"]:
                lines.append(f"*{data['message']}*\n")
            if data["result"]:
                lines.append("```")
                lines.append(data["result"])
                lines.append("```\n")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# HTML renderer
# ---------------------------------------------------------------------------

CSS = """
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; max-width: 960px;
         margin: 2rem auto; padding: 0 1rem; color: #1a1a1a; }
  h1   { border-bottom: 2px solid #0066cc; padding-bottom: .4rem; }
  h2   { margin-top: 2rem; }
  .user     { background: #e8f0fe; border-left: 4px solid #4285f4;
              padding: .8rem 1rem; border-radius: 4px; margin-bottom: 1rem; }
  .response { background: #f8f9fa; border-left: 4px solid #34a853;
              padding: .8rem 1rem; border-radius: 4px; margin-bottom: 1rem; }
  .tool-ok  { background: #e6f4ea; border-left: 4px solid #34a853;
              padding: .6rem 1rem; border-radius: 4px; margin-bottom: .6rem; }
  .tool-err { background: #fce8e6; border-left: 4px solid #ea4335;
              padding: .6rem 1rem; border-radius: 4px; margin-bottom: .6rem; }
  .think    { background: #fff8e1; border-left: 4px solid #fbbc04;
              padding: .6rem 1rem; border-radius: 4px; margin-bottom: .6rem; }
  details summary { cursor: pointer; font-weight: bold; }
  pre  { background: #f1f3f4; padding: .8rem; border-radius: 4px;
         overflow-x: auto; white-space: pre-wrap; }
  code { background: #f1f3f4; padding: .1rem .3rem; border-radius: 3px; }
  hr   { border: none; border-top: 1px solid #dadce0; margin: 2rem 0; }
  .meta { font-size: .85em; color: #666; margin-bottom: .3rem; }
</style>
"""


def md_to_html_simple(text: str) -> str:
    """Very lightweight Markdown → HTML conversion for response blocks."""
    esc = html_module.escape(text)
    # code blocks
    esc = re.sub(r"```[^\n]*\n(.*?)```", lambda m: f"<pre>{m.group(1)}</pre>", esc, flags=re.DOTALL)
    # inline code
    esc = re.sub(r"`([^`]+)`", r"<code>\1</code>", esc)
    # bold
    esc = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc)
    # italic
    esc = re.sub(r"\*(.+?)\*", r"<em>\1</em>", esc)
    # headers
    esc = re.sub(r"^### (.+)$", r"<h3>\1</h3>", esc, flags=re.MULTILINE)
    esc = re.sub(r"^## (.+)$", r"<h2>\1</h2>", esc, flags=re.MULTILINE)
    esc = re.sub(r"^# (.+)$", r"<h1>\1</h1>", esc, flags=re.MULTILINE)
    # paragraphs
    paragraphs = esc.split("\n\n")
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith("<"):
            html_parts.append(p)
        else:
            html_parts.append(f"<p>{p.replace(chr(10), '<br>')}</p>")
    return "\n".join(html_parts)


def render_html(blocks: list, title: str = "Chat Summary") -> str:
    parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        f"  <meta charset='UTF-8'>",
        f"  <title>{html_module.escape(title)}</title>",
        CSS,
        "</head>",
        "<body>",
        f"<h1>{html_module.escape(title)}</h1>",
    ]

    for kind, data in blocks:
        if kind == "hr":
            parts.append("<hr>")
        elif kind == "user":
            ts = f"<span class='meta'>{html_module.escape(data['timestamp'])}</span><br>" if data["timestamp"] else ""
            model = f"<span class='meta'>Model: <code>{html_module.escape(data['model'])}</code></span><br>" if data["model"] else ""
            parts.append(f"<div class='user'>")
            parts.append(f"<strong>👤 User Request</strong><br>{ts}{model}")
            parts.append(f"<p>{html_module.escape(data['text']).replace(chr(10), '<br>')}</p>")
            parts.append("</div>")
        elif kind == "response":
            parts.append("<div class='response'>")
            parts.append("<strong>🤖 GitHub Copilot</strong>")
            parts.append(md_to_html_simple(data["text"]))
            parts.append("</div>")
        elif kind == "think":
            title_str = html_module.escape(data.get("title", "Thinking") or "Thinking")
            parts.append("<div class='think'>")
            parts.append(f"<details><summary>🤔 {title_str}</summary>")
            parts.append(f"<p>{html_module.escape(data['text']).replace(chr(10), '<br>')}</p>")
            parts.append("</details></div>")
        elif kind == "tool":
            cls = "tool-ok" if data["success"] else "tool-err"
            icon = "✅" if data["success"] else "❌"
            parts.append(f"<div class='{cls}'>")
            parts.append(f"<strong>{icon} Tool: <code>{html_module.escape(data['name'])}</code></strong>")
            if data["message"]:
                parts.append(f"<p><em>{html_module.escape(data['message'])}</em></p>")
            if data["result"]:
                parts.append(f"<pre>{html_module.escape(data['result'])}</pre>")
            parts.append("</div>")

    parts += ["</body>", "</html>"]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# LaTeX renderer
# ---------------------------------------------------------------------------

def latex_escape(text: str) -> str:
    """Escape special LaTeX characters."""
    replacements = [
        ("\\", r"\textbackslash{}"),
        ("&",  r"\&"),
        ("%",  r"\%"),
        ("$",  r"\$"),
        ("#",  r"\#"),
        ("_",  r"\_"),
        ("{",  r"\{"),
        ("}",  r"\}"),
        ("~",  r"\textasciitilde{}"),
        ("^",  r"\textasciicircum{}"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


LATEX_PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{xcolor}
\usepackage{mdframed}
\usepackage{listings}
\usepackage{hyperref}
\usepackage{parskip}

\definecolor{userblue}{RGB}{66,133,244}
\definecolor{copilotgreen}{RGB}{52,168,83}
\definecolor{toolorange}{RGB}{251,188,4}
\definecolor{toolerrred}{RGB}{234,67,53}
\definecolor{thinkbg}{RGB}{255,248,225}
\definecolor{userbg}{RGB}{232,240,254}
\definecolor{copbg}{RGB}{248,249,250}
\definecolor{toolokbg}{RGB}{230,244,234}
\definecolor{toolerrbg}{RGB}{252,232,230}

\lstset{
  basicstyle=\ttfamily\small,
  breaklines=true,
  breakatwhitespace=true,
  frame=single,
  backgroundcolor=\color{userbg!30},
}

\newmdenv[backgroundcolor=userbg, linecolor=userblue, linewidth=2pt,
  leftline=true, rightline=false, topline=false, bottomline=false,
  innerleftmargin=8pt]{userbox}

\newmdenv[backgroundcolor=copbg, linecolor=copilotgreen, linewidth=2pt,
  leftline=true, rightline=false, topline=false, bottomline=false,
  innerleftmargin=8pt]{copilotbox}

\newmdenv[backgroundcolor=toolokbg, linecolor=copilotgreen, linewidth=2pt,
  leftline=true, rightline=false, topline=false, bottomline=false,
  innerleftmargin=8pt]{toolokbox}

\newmdenv[backgroundcolor=toolerrbg, linecolor=toolerrred, linewidth=2pt,
  leftline=true, rightline=false, topline=false, bottomline=false,
  innerleftmargin=8pt]{toolerrbox}

\newmdenv[backgroundcolor=thinkbg, linecolor=toolorange, linewidth=2pt,
  leftline=true, rightline=false, topline=false, bottomline=false,
  innerleftmargin=8pt]{thinkbox}

\title{Chat Summary}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage
"""

LATEX_END = r"\end{document}"

REQUEST_COUNTER = [0]  # mutable for use inside render


def render_latex(blocks: list) -> str:
    parts = [LATEX_PREAMBLE]
    req_idx = 0

    for kind, data in blocks:
        if kind == "hr":
            parts.append(r"\bigskip\hrule\bigskip")
            req_idx += 1
        elif kind == "user":
            req_idx += 1
            ts = f"\\textit{{{latex_escape(data['timestamp'])}}}" if data["timestamp"] else ""
            model = f"\\texttt{{{latex_escape(data['model'])}}}" if data["model"] else ""
            label = f"Request {req_idx}"
            parts.append(f"\\section{{{latex_escape(label)}}}")
            parts.append(r"\begin{userbox}")
            parts.append(f"\\textbf{{User Request}}")
            if ts:
                parts.append(f"\\quad {ts}")
            if model:
                parts.append(f"\\quad Model: {model}")
            parts.append("")
            # Split into paragraphs
            for para in data["text"].split("\n\n"):
                para = para.strip()
                if para:
                    parts.append(latex_escape(para) + "\n")
            parts.append(r"\end{userbox}")
        elif kind == "response":
            parts.append(r"\begin{copilotbox}")
            parts.append(r"\textbf{GitHub Copilot:}")
            parts.append("")
            for para in data["text"].split("\n\n"):
                para = para.strip()
                if not para:
                    continue
                # Detect code block
                if para.startswith("```"):
                    code = re.sub(r"^```[^\n]*\n?", "", para)
                    code = re.sub(r"```$", "", code).strip()
                    parts.append(r"\begin{lstlisting}")
                    parts.append(code)
                    parts.append(r"\end{lstlisting}")
                else:
                    parts.append(latex_escape(para) + "\n")
            parts.append(r"\end{copilotbox}")
        elif kind == "think":
            title_str = latex_escape(data.get("title", "Thinking") or "Thinking")
            parts.append(r"\begin{thinkbox}")
            parts.append(f"\\textbf{{Thinking:}} \\textit{{{title_str}}}")
            parts.append("")
            for para in data["text"].split("\n\n"):
                para = para.strip()
                if para:
                    parts.append(latex_escape(para) + "\n")
            parts.append(r"\end{thinkbox}")
        elif kind == "tool":
            env = "toolokbox" if data["success"] else "toolerrbox"
            icon = r"\checkmark" if data["success"] else r"\textbf{ERROR}"
            parts.append(f"\\begin{{{env}}}")
            parts.append(
                f"\\textbf{{Tool:}} \\texttt{{{latex_escape(data['name'])}}} "
                f"({icon})"
            )
            if data["message"]:
                parts.append(f"\\textit{{{latex_escape(data['message'])}}}")
            if data["result"]:
                parts.append(r"\begin{lstlisting}")
                # truncate very long results
                result_text = data["result"]
                if len(result_text) > 3000:
                    result_text = result_text[:3000] + "\n... [truncated]"
                parts.append(result_text)
                parts.append(r"\end{lstlisting}")
            parts.append(f"\\end{{{env}}}")

    parts.append(LATEX_END)
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    chat_path = args.chat_file
    fmt = args.format

    if not os.path.exists(chat_path):
        print(f"Error: file not found: {chat_path}")
        sys.exit(1)

    try:
        chat_data = load_chat(chat_path)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON – {e}")
        sys.exit(1)

    blocks = build_document(chat_data)
    out_dir = os.path.dirname(os.path.abspath(chat_path))
    stem = Path(chat_path).stem  # usually "chat"

    produced = []

    if fmt in ("md", "all"):
        md_text = render_markdown(blocks)
        md_path = os.path.join(out_dir, f"{stem}_summary.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        produced.append(md_path)

    if fmt in ("html", "all"):
        html_text = render_html(blocks)
        html_path = os.path.join(out_dir, f"{stem}_summary.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_text)
        produced.append(html_path)

    if fmt in ("latex", "all"):
        latex_text = render_latex(blocks)
        latex_path = os.path.join(out_dir, f"{stem}_summary.tex")
        with open(latex_path, "w", encoding="utf-8") as f:
            f.write(latex_text)
        produced.append(latex_path)

    for p in produced:
        print(f"Written: {p}")


if __name__ == "__main__":
    main()

