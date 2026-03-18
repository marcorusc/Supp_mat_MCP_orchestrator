#!/usr/bin/env python3
"""
generate_chat_summaries.py

For every chat_summary.md found under */Scenario_*/ (excluding deprecated/),
strips LLM thinking blocks, extracts user prompts and MCP tool calls, and
writes chat_summary_cleaned.md in the same folder.

Usage:
    python generate_chat_summaries.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent

# ── Constants ─────────────────────────────────────────────────────────────────

# Files / patterns to skip when listing generated outputs
_EXCLUDE_NAMES = {
    "chat.json",
    "chat_summary.md",
    "chat_summary.html",
    "chat_summary.tex",
    "chat_summary_cleaned.md",
}
_EXCLUDE_SUFFIXES = {".md", ".html", ".tex"}
_EXCLUDE_CSV_RE   = re.compile(r".*_(chat_summary|tool_metrics)\.csv$")
_EXCLUDE_MCP_RE   = re.compile(r"updated_MCP_.*\.csv$")

# Pipeline-stage tool prefixes
_NEKO_PREFIX      = "mcp_neko_"
_MABOSS_PREFIX    = "mcp_maboss_"
_PHYSICELL_PREFIX = "mcp_physicell_"

# Outcomes that are bare labels / section headings carrying no useful data
_UNINFORMATIVE_EXACT = {
    "## Simulation Summary",
    "## XML Configuration Exported",
    "## Cell Rules CSV Exported",
}
# Bare label lines, plain or bold-formatted:
#   "Network nodes:"  |  "**Cell rule added:**"  |  "**Simulation domain created (2D):**"
_BARE_LABEL_RE = re.compile(r"^(\*\*)?[A-Za-z][A-Za-z0-9 _/()*\-,]*:(\*\*)?\s*$")

# Artifact extensions to list and their descriptions
_ARTIFACT_SUFFIXES = {".bnet", ".bnd", ".cfg", ".xml", ".csv"}
_ARTIFACT_DESCRIPTIONS = {
    ".bnet": "Boolean network (BNET format)",
    ".bnd":  "MaBoSS logical rules file",
    ".cfg":  "MaBoSS configuration file",
    ".xml":  "PhysiCell XML simulation configuration",
    ".csv":  "Cell rules / simulation data (CSV)",
}

# Human-readable LLM names
_MODEL_MAP = {
    "claude-sonnet-4": "Claude Sonnet 4",
    "gpt-5.1":         "GPT-5.1",
    "o4-mini":         "GPT-o4-mini",
}
_FOLDER_MAP = {
    "Sonnet_4":    "Claude Sonnet 4",
    "Gpt_5":       "GPT-5.1",
    "Gpt_o4_mini": "GPT-o4-mini",
}

# Canned 2–3 sentence workflow descriptions keyed by detected pipeline stages
_WORKFLOW_DESCRIPTIONS: dict[tuple[str, ...], str] = {
    ("NeKo", "MaBoSS", "PhysiCell/PhysiBoSS"): (
        "This transcript covers the one-shot construction of a multiscale "
        "TNF-response workflow. The agent infers a cancer-cell gene regulatory "
        "network using NeKo (OmniPath), converts it to a Boolean model in MaBoSS, "
        "and integrates it into a PhysiCell multicellular simulation via PhysiBoSS."
    ),
    ("NeKo", "MaBoSS"): (
        "This transcript covers the one-shot construction of a Boolean network "
        "model of TNF-response cell fate. The agent infers a gene regulatory "
        "network using NeKo (OmniPath) and simulates it with MaBoSS to assess "
        "apoptotic and proliferative attractors."
    ),
    ("PhysiCell/PhysiBoSS",): (
        "This transcript covers the automated extension of an existing PhysiCell "
        "simulation configuration. The agent loads the XML model, analyses the "
        "biological scenario, and adds biologically grounded cell-behaviour rules "
        "covering substrate responses, cell–cell interactions, and fate decisions."
    ),
    ("MaBoSS",): (
        "This transcript covers Boolean network simulation using MaBoSS, building "
        "and analysing attractors for a TNF-response cancer cell fate model."
    ),
}


# ── Small helpers ─────────────────────────────────────────────────────────────

def _format_llm(folder_name: str, model_string: str) -> str:
    for key, display in _MODEL_MAP.items():
        if key in model_string:
            return display
    return _FOLDER_MAP.get(folder_name, folder_name)


def _extract_model_string(text: str) -> str:
    m = re.search(r"## 👤 User Request\s+\*[^*]+\*\s+`([^`]+)`", text)
    return m.group(1) if m else ""


def _is_informative(line: str) -> bool:
    """Return False for bare headings / label-only lines."""
    if not line:
        return False
    if line in _UNINFORMATIVE_EXACT:
        return False
    if _BARE_LABEL_RE.match(line):
        return False
    return True


def _is_artifact(path: Path) -> bool:
    name = path.name
    if name in _EXCLUDE_NAMES:
        return False
    if path.suffix in _EXCLUDE_SUFFIXES:
        return False
    if _EXCLUDE_CSV_RE.match(name) or _EXCLUDE_MCP_RE.match(name):
        return False
    return path.suffix in _ARTIFACT_SUFFIXES


# ── Extraction ────────────────────────────────────────────────────────────────

def strip_thinking_blocks(text: str) -> str:
    """Remove all <details>…</details> blocks used for LLM reasoning."""
    return re.sub(r"<details>.*?</details>", "", text, flags=re.DOTALL)


def extract_user_requests(text: str) -> list[tuple[str, str]]:
    """Return list of (timestamp, request_text) for every user turn."""
    header_re = re.compile(
        r"## 👤 User Request\s+\*([\d\-: A-Z]+)\*\s+`[^`]+`"
    )
    headers = list(header_re.finditer(text))
    results = []
    for i, m in enumerate(headers):
        timestamp = m.group(1).strip()
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[start:end]
        body = re.split(r"\*\*GitHub Copilot:\*\*|\*\*✅ Tool:", body)[0]
        body = body.strip()
        if body:
            results.append((timestamp, body))
    return results


def extract_tool_calls(text: str) -> list[tuple[str, str]]:
    """
    Return list of (tool_name, first_informative_output_line).

    Only MCP tools (names starting with 'mcp_') are included.
    """
    segments = re.split(r"(?=\*\*✅ Tool: `)", text)
    results = []
    for seg in segments:
        m = re.match(r"\*\*✅ Tool: `([^`]+)`\*\*\s*\n(.*)", seg, re.DOTALL)
        if not m:
            continue
        tool_name = m.group(1).strip()
        rest = m.group(2)
        if not tool_name.startswith("mcp_"):
            continue

        code_match = re.search(r"```[^\n]*\n(.*?)```", rest, re.DOTALL)
        first_line = ""
        if code_match:
            for ln in code_match.group(1).splitlines():
                ln = ln.strip()
                if ln in ("{", "}", "[", "]", "{}", "[]"):
                    continue
                if _is_informative(ln):
                    first_line = ln
                    break

        # Strip private absolute path prefix
        first_line = first_line.replace("/home/mruscone/Desktop/github/", "")

        if len(first_line) > 120:
            first_line = first_line[:117] + "…"

        results.append((tool_name, first_line))
    return results


def deduplicate_tool_calls(
    calls: list[tuple[str, str]],
) -> list[tuple[str, str]]:
    """
    Drop redundant calls:
    - Empty-outcome calls are dropped if the tool already has a non-empty result.
    - Exact (tool, outcome) duplicate pairs are dropped (re-run artefacts).
    - Calls with distinct non-empty outcomes are always kept (e.g. repeated
      add_physiboss_output_link or add_single_cell_rule with different rules).
    """
    seen_pairs: set[tuple[str, str]] = set()
    seen_nonempty: set[str] = set()
    result = []
    for tool, outcome in calls:
        if outcome == "" and tool in seen_nonempty:
            continue  # empty re-run after a successful call
        key = (tool, outcome)
        if key in seen_pairs:
            continue  # exact duplicate
        seen_pairs.add(key)
        if outcome:
            seen_nonempty.add(tool)
        result.append((tool, outcome))
    return result


# ── Workflow summary ──────────────────────────────────────────────────────────

def _detect_stages(tool_calls: list[tuple[str, str]]) -> tuple[str, ...]:
    tools = {t for t, _ in tool_calls}
    stages = []
    if any(t.startswith(_NEKO_PREFIX) for t in tools):
        stages.append("NeKo")
    if any(t.startswith(_MABOSS_PREFIX) for t in tools):
        stages.append("MaBoSS")
    if any(t.startswith(_PHYSICELL_PREFIX) for t in tools):
        stages.append("PhysiCell/PhysiBoSS")
    return tuple(stages)


def generate_workflow_summary(
    llm_display: str,
    scenario_display: str,
    tool_calls: list[tuple[str, str]],
) -> str:
    stages = _detect_stages(tool_calls)
    description = _WORKFLOW_DESCRIPTIONS.get(
        stages,
        "This transcript documents an automated multiscale modelling session.",
    )
    return description


# ── Generated outputs ─────────────────────────────────────────────────────────

def list_generated_outputs(folder: Path) -> list[tuple[str, str]]:
    """Return (filename, description) pairs for modelling artefacts."""
    results = []
    for p in sorted(folder.iterdir()):
        if not p.is_file():
            continue
        if _is_artifact(p):
            desc = _ARTIFACT_DESCRIPTIONS.get(p.suffix, "")
            results.append((p.name, desc))
    return results


# ── Main assembly ─────────────────────────────────────────────────────────────

def clean_chat_summary(src: Path) -> None:
    """Process one chat_summary.md and write chat_summary_cleaned.md next to it."""
    text = src.read_text(encoding="utf-8")

    scenario_folder  = src.parts[-2]                        # "Scenario_1"
    llm_folder       = src.parts[-3]                        # "Sonnet_4"
    model_string     = _extract_model_string(text)
    llm_display      = _format_llm(llm_folder, model_string)
    scenario_num     = scenario_folder.split("_")[-1]       # "1"
    scenario_display = f"Scenario {scenario_num}"

    text = strip_thinking_blocks(text)

    user_requests = extract_user_requests(text)
    tool_calls    = deduplicate_tool_calls(extract_tool_calls(text))
    # Keep only rows that have a real informative outcome
    tool_calls    = [(t, o) for t, o in tool_calls if o]

    out: list[str] = []

    # ── title ──────────────────────────────────────────────────────────────────
    out.append(f"# {scenario_display} — {llm_display}\n")

    # ── workflow summary ───────────────────────────────────────────────────────
    out.append("## Workflow summary\n")
    out.append(generate_workflow_summary(llm_display, scenario_display, tool_calls) + "\n")

    # ── user prompts ───────────────────────────────────────────────────────────
    if user_requests:
        initial_ts, initial_req = user_requests[0]
        continuations = user_requests[1:]

        out.append("## Initial prompt\n")
        out.append(f"_{initial_ts}_\n")
        out.append(initial_req + "\n")

        if continuations:
            out.append("## Continuation prompts\n")
            for ts, req in continuations:
                # Inline short messages; block-quote longer ones
                req_short = req.replace("\n", " ").strip()
                out.append(f"- _{ts}_ — {req_short}\n")
    else:
        out.append("## Initial prompt\n")
        out.append("_Not found._\n")

    # ── tool-call table ────────────────────────────────────────────────────────
    out.append("## MCP tool calls\n")
    if tool_calls:
        out.append("| # | Tool | Outcome |")
        out.append("|---|------|---------|")
        for i, (tool, outcome) in enumerate(tool_calls, start=1):
            outcome_md = outcome.replace("|", "\\|")
            out.append(f"| {i} | `{tool}` | {outcome_md} |")
    else:
        out.append("_No MCP tool calls with informative output found._")

    # ── generated outputs ──────────────────────────────────────────────────────
    artifacts = list_generated_outputs(src.parent)
    out.append("\n## Generated outputs\n")
    if artifacts:
        for fname, desc in artifacts:
            desc_part = f" — {desc}" if desc else ""
            out.append(f"- `{fname}`{desc_part}")
    else:
        out.append("_No modelling artefacts detected in this folder._")

    dst = src.parent / "chat_summary_cleaned.md"
    dst.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"  ✓  {dst.relative_to(ROOT)}")


def main() -> None:
    summaries = sorted(ROOT.glob("*/Scenario_*/chat_summary.md"))
    summaries = [p for p in summaries if "deprecated" not in p.parts]

    if not summaries:
        print("No chat_summary.md files found.")
        return

    print(f"Processing {len(summaries)} chat summary file(s)…\n")
    for src in summaries:
        clean_chat_summary(src)
    print("\nDone.")


if __name__ == "__main__":
    main()
