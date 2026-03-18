#!/usr/bin/env python3
"""
summaries_to_latex.py

Converts all chat_summary_cleaned.md files found under */Scenario_*/
into LaTeX fragment files (chat_summary_cleaned.tex), one per file.

Usage:
    python summaries_to_latex.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent

UNICODE_LATEX_MAP = {
    '…': r'\ldots{}',
    '×': r'\times{}',
    'μ': r'\ensuremath{\mu}',
    'µ': r'\ensuremath{\mu}',
    '³': r'\textsuperscript{3}',
    '²': r'\textsuperscript{2}',
    '⁻': r'\textsuperscript{-}',
    '¹': r'\textsuperscript{1}',
    '→': r'\ensuremath{\rightarrow}',
    '↔': r'\ensuremath{\leftrightarrow}',
    '≤': r'\ensuremath{\leq}',
    '≥': r'\ensuremath{\geq}',
    'α': r'\ensuremath{\alpha}',
    'β': r'\ensuremath{\beta}',
}


# ── LaTeX helpers ──────────────────────────────────────────────────────────────

def latex_escape(text: str) -> str:
    """
    Escape LaTeX special characters in a single regex pass to avoid
    double-escaping (e.g. the { } inside \\textbackslash{} getting escaped).
    """
    mapping = {
        '\\': r'\textbackslash{}',
        '&':  r'\&',
        '%':  r'\%',
        '$':  r'\$',
        '#':  r'\#',
        '_':  r'\_',
        '{':  r'\{',
        '}':  r'\}',
        '~':  r'\textasciitilde{}',
        '^':  r'\textasciicircum{}',
    }
    text = re.sub(r'[\\&%$#_{}\~\^]', lambda m: mapping[m.group()], text)
    for char, replacement in UNICODE_LATEX_MAP.items():
        text = text.replace(char, replacement)
    return text


def strip_md_inline(text: str) -> str:
    """Remove lightweight Markdown formatting while keeping the raw content."""
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[-*]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    return text.strip()


def md_to_tex_inline(text: str) -> str:
    """Strip Markdown inline decoration, then LaTeX-escape the result."""
    text = strip_md_inline(text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    return latex_escape(text.strip())


def tex_escape_code(text: str) -> str:
    """Escape code-like strings and add breakpoints after common separators."""
    pieces: list[str] = []
    for char in text:
        if char in UNICODE_LATEX_MAP:
            pieces.append(UNICODE_LATEX_MAP[char])
        elif char == '\\':
            pieces.append(r'\textbackslash{}')
        elif char == '&':
            pieces.append(r'\&')
        elif char == '%':
            pieces.append(r'\%')
        elif char == '$':
            pieces.append(r'\$')
        elif char == '#':
            pieces.append(r'\#')
        elif char == '_':
            pieces.append(r'\_\allowbreak{}')
        elif char == '{':
            pieces.append(r'\{')
        elif char == '}':
            pieces.append(r'\}')
        elif char == '~':
            pieces.append(r'\textasciitilde{}')
        elif char == '^':
            pieces.append(r'\textasciicircum{}')
        elif char in '/.-:=()[]':
            pieces.append(char + r'\allowbreak{}')
        else:
            pieces.append(char)
    return ''.join(pieces)


def md_backtick_to_texttt(text: str) -> str:
    """Convert `code` spans to \\texttt{…} and LaTeX-escape surrounding text."""
    parts = re.split(r'`([^`]+)`', text)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:          # odd indices are inside backticks
            result.append(r'\texttt{' + tex_escape_code(part) + r'}')
        else:
            result.append(latex_escape(part))
    return ''.join(result)


def md_inline_to_tex(text: str) -> str:
    """Convert inline Markdown to LaTeX while preserving code spans."""
    return md_backtick_to_texttt(strip_md_inline(text))


def format_tool_cell(text: str) -> str:
    """Format code-like tool names for table cells."""
    return r'\texttt{' + tex_escape_code(text) + r'}'


# ── Section extractors ─────────────────────────────────────────────────────────

def _extract_section(text: str, header: str) -> str:
    """Return the body of the named ## section (stripped), or ''."""
    pattern = rf'## {re.escape(header)}\s+(.*?)(?=\n## |\Z)'
    m = re.search(pattern, text, flags=re.DOTALL)
    return m.group(1).strip() if m else ''


def extract_title(text: str) -> str:
    m = re.search(r'^#\s+(.*)$', text, flags=re.MULTILINE)
    return m.group(1).strip() if m else 'Chat summary'


def extract_workflow(text: str) -> str:
    return _extract_section(text, 'Workflow summary')


def extract_initial_prompt(text: str) -> tuple[str, str]:
    """Return (timestamp, prompt_body) — timestamp may be ''."""
    block = _extract_section(text, 'Initial prompt')
    lines = block.splitlines()
    timestamp = ''
    body_lines = []
    for i, line in enumerate(lines):
        ts_m = re.match(r'^_([\d\-: A-Z]+)_\s*$', line.strip())
        if ts_m and i == 0:
            timestamp = ts_m.group(1).strip()
        else:
            body_lines.append(line)
    return timestamp, '\n'.join(body_lines).strip()


def extract_continuation_prompts(text: str) -> list[tuple[str, str]]:
    """Return list of (timestamp, message_text)."""
    block = _extract_section(text, 'Continuation prompts')
    results = []
    for line in block.splitlines():
        line = line.strip()
        if not (line.startswith('-') or line.startswith('*')):
            continue
        line = line[1:].strip()
        # Format: _timestamp_ — message
        m = re.match(r'^_([\d\-: A-Z]+)_\s*[—\-]+\s*(.+)$', line)
        if m:
            results.append((m.group(1).strip(), m.group(2).strip()))
        else:
            results.append(('', line))
    return results


def extract_tool_rows(text: str) -> list[tuple[str, str, str]]:
    """Return list of (step, tool_name, outcome) parsed from the tool-call table."""
    block = _extract_section(text, 'MCP tool calls')
    rows = []
    for line in block.splitlines():
        if not line.startswith('|'):
            continue
        if re.search(r'-{3,}', line):      # separator row (|---|...)
            continue
        # Split only on | NOT preceded by \ so that \| inside cells is preserved
        parts = [p.strip() for p in re.split(r'(?<!\\)\|', line.strip('|'))]
        if len(parts) < 3:
            continue
        step = parts[0]
        tool = parts[1]
        # Rejoin in case the outcome cell itself contained \| sequences
        outcome = '|'.join(p.strip() for p in parts[2:]).strip()
        # Restore escaped pipes to real pipes for display
        outcome = outcome.replace(r'\|', '|')
        if step == '#':                     # header row
            continue
        # Strip surrounding backticks from tool name (column is already \ttfamily)
        tool = re.sub(r'^`(.*)`$', r'\1', tool)
        rows.append((step, tool, outcome))
    return rows


def extract_outputs(text: str) -> list[str]:
    """Return raw output lines (with Markdown intact for backtick conversion)."""
    block = _extract_section(text, 'Generated outputs')
    results = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith('-') or line.startswith('*'):
            results.append(line[1:].strip())
    return results


# ── Main converter ─────────────────────────────────────────────────────────────

def md_summary_to_tex(md_path: Path) -> str:
    text = md_path.read_text(encoding='utf-8')

    title         = extract_title(text)
    workflow      = extract_workflow(text)
    ts, prompt    = extract_initial_prompt(text)
    continuations = extract_continuation_prompts(text)
    tool_rows     = extract_tool_rows(text)
    outputs       = extract_outputs(text)

    out: list[str] = []

    # ── title ──────────────────────────────────────────────────────────────────
    out.append(r'\subsection{' + latex_escape(title) + r'}')
    out.append('')

    # ── workflow summary ───────────────────────────────────────────────────────
    if workflow:
        out.append(r'\paragraph{Workflow summary}')
        out.append(md_to_tex_inline(workflow))
        out.append('')

    # ── initial prompt ─────────────────────────────────────────────────────────
    if prompt:
        label = r'\paragraph{Initial prompt}'
        if ts:
            label += r' \hfill \textit{\small ' + latex_escape(ts) + r'}'
        out.append(label)
        out.append(r'\begin{quote}')
        out.append(md_to_tex_inline(prompt))
        out.append(r'\end{quote}')
        out.append('')

    # ── continuation prompts ───────────────────────────────────────────────────
    if continuations:
        out.append(r'\paragraph{Continuation prompts}')
        out.append(r'\begin{itemize}')
        for cont_ts, msg in continuations:
            msg_tex = md_to_tex_inline(msg)
            if cont_ts:
                msg_tex = (r'\textit{\small ' + latex_escape(cont_ts)
                           + r'} --- ' + msg_tex)
            out.append(r'\item ' + msg_tex)
        out.append(r'\end{itemize}')
        out.append('')

    # ── tool call table ────────────────────────────────────────────────────────
    if tool_rows:
        out.append(r'\paragraph{MCP tool calls}')
        out.append(r'\begingroup')
        out.append(r'\small')
        out.append(r'\setlength{\itemsep}{5pt}')
        out.append(r'\setlength{\parskip}{0pt}')
        out.append(r'\begin{enumerate}')
        for step, tool, outcome in tool_rows:
            tool_tex    = format_tool_cell(tool)
            outcome_tex = md_inline_to_tex(outcome)
            out.append(r'\item[' + latex_escape(step) + r'.] ' + tool_tex)
            out.append(r'\hfill\\')
            out.append(r'\RaggedRight ' + outcome_tex)
        out.append(r'\end{enumerate}')
        out.append(r'\endgroup')
        out.append('')

    # ── generated outputs ──────────────────────────────────────────────────────
    if outputs:
        out.append(r'\paragraph{Generated outputs}')
        out.append(r'\begin{itemize}')
        for item in outputs:
            out.append(r'\item ' + md_backtick_to_texttt(item))
        out.append(r'\end{itemize}')
        out.append('')

    return '\n'.join(out)


def main() -> None:
    summaries = sorted(ROOT.glob('*/Scenario_*/chat_summary_cleaned.md'))
    summaries = [p for p in summaries if 'deprecated' not in p.parts]

    if not summaries:
        print('No chat_summary_cleaned.md files found.')
        return

    print(f'Converting {len(summaries)} file(s)…\n')
    for src in summaries:
        tex = md_summary_to_tex(src)
        dst = src.with_suffix('.tex')
        dst.write_text(tex, encoding='utf-8')
        print(f'  ✓  {dst.relative_to(ROOT)}')
    print('\nDone.')


if __name__ == '__main__':
    main()
