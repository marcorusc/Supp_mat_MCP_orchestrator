"""
metrics_extractor.py  –  Extract reproducibility & performance metrics from a
GitHub Copilot chat export (JSON format) and write two CSV files:

  <model>_<scenario>_chat_summary.csv   – ONE row summarising the whole conversation
  <model>_<scenario>_tool_metrics.csv   – one row per tool-call attempt

Usage:
    python metrics_extractor.py <chat_file.json>

Chat-summary columns
--------------------
  model, scenario                – inferred from the file path
  model_id                       – e.g. copilot/claude-sonnet-4
  chat_file                      – relative path to the source JSON
  has_token_counts               – False for old client exports (deprecated chats)
  timestamp_start_utc            – UTC time of the first user message
  timestamp_end_utc              – UTC time of the last user message
  total_wall_time_s              – sum of server-side elapsed time across all requests (seconds)
  total_requests                 – total number of user messages in the conversation
  n_human_interventions          – requests beyond the first (= total_requests - 1)
  n_max_tools_exceeded           – times VS Code cut off tool calls, forcing a re-prompt
  total_tool_calls               – all tool invocations across the conversation
  total_tool_calls_success       – calls that did NOT return an ERROR
  total_tool_calls_failed        – calls that returned an ERROR
  tool_success_rate_pct          – 100 * success / total  (empty if no calls)
  total_retries                  – sum of toolInputRetry across all calls
  total_prompt_tokens            – billed input tokens  (empty if not tracked)
  total_completion_tokens        – billed output tokens (empty if not tracked)
  total_tokens                   – prompt + completion  (empty if not tracked)

Not available in the export: temperature, seed, prompt/tool version, compute cost.
    Compute cost can be derived externally by multiplying token counts by per-model pricing.

Per-tool columns
----------------
  request_index, round_index, tool_name, tool_call_id,
  retry_count, success, error_msg, response_preview
"""

import json
import csv
import sys
import os
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def parse_model_scenario(chat_path: str):
    """Infer model and scenario labels from the file path.

    Handles paths like:
      gpt_5/Scenario_1/chat.json          → model=gpt_5,    scenario=Scenario_1
      Sonnet4/Scenario_2/chat.json        → model=Sonnet4,   scenario=Scenario_2
      updated_MCP/Sonnet_4/Scenario_1/...→ model=Sonnet_4,   scenario=Scenario_1

    Rule: scenario = immediate parent dir of chat.json;
          model    = one level above the scenario dir.
    """
    parts = Path(chat_path).resolve().parts[:-1]  # drop the filename
    scenario = parts[-1] if parts else "UnknownScenario"
    model = parts[-2] if len(parts) >= 2 else "UnknownModel"
    return model, scenario


def is_error_result(result_value: str) -> bool:
    if not isinstance(result_value, str):
        return False
    return result_value.strip().startswith("ERROR")


def extract_tool_result_text(result_details: dict) -> str:
    """Return the text of the first result output item."""
    outputs = result_details.get("output", [])
    for o in outputs:
        if isinstance(o, dict) and "value" in o and isinstance(o["value"], str):
            return o["value"]
    return ""


# ---------------------------------------------------------------------------
# main extraction
# ---------------------------------------------------------------------------

def extract_metrics(chat_data: dict, chat_path: str):
    """Return (summary_row: dict, tool_rows: list[dict])."""
    requests = chat_data.get("requests", [])

    # ── accumulators ────────────────────────────────────────────────────────
    model_id = ""
    timestamps = []

    total_elapsed_ms   = 0
    has_elapsed        = False

    total_prompt_tokens      = 0
    total_completion_tokens  = 0
    has_token_counts         = False

    total_tool_calls   = 0
    total_success      = 0
    total_failed       = 0
    total_retries      = 0
    n_max_exceeded     = 0

    tool_rows = []

    for req_idx, req in enumerate(requests):
        if not model_id:
            model_id = req.get("modelId", "")

        ts = req.get("timestamp")
        if ts is not None:
            timestamps.append(ts)

        result   = req.get("result", {}) or {}
        timings  = result.get("timings", {}) or {}
        metadata = result.get("metadata", {}) or {}
        usage    = result.get("usage", {}) or {}

        elapsed = timings.get("totalElapsed")
        if elapsed is not None:
            total_elapsed_ms += elapsed
            has_elapsed = True

        pt = usage.get("promptTokens")
        ct = usage.get("completionTokens")
        if pt is not None or ct is not None:
            has_token_counts = True
            total_prompt_tokens     += pt or 0
            total_completion_tokens += ct or 0

        if metadata.get("maxToolCallsExceeded"):
            n_max_exceeded += 1

        # ── tool calls from result.metadata.toolCallRounds (Claude/new export)
        for round_idx, rnd in enumerate(metadata.get("toolCallRounds", [])):
            tc_results       = rnd.get("toolCallResults", {})
            response_preview = str(rnd.get("response", ""))[:200]

            for tc in rnd.get("toolCalls", []):
                tc_id   = tc.get("id", "")
                tc_name = tc.get("name", "")
                retry   = tc.get("toolInputRetry", 0)
                is_mcp  = tc_name.startswith("mcp_")

                result_text = ""
                entry = tc_results.get(tc_id)
                if entry:
                    for c in entry.get("content", []):
                        if isinstance(c, dict) and isinstance(c.get("value"), str):
                            result_text = c["value"]
                            break

                success = not is_error_result(result_text)

                # Only MCP tools contribute to the headline counters
                if is_mcp:
                    total_retries    += retry
                    total_tool_calls += 1
                    if success:
                        total_success += 1
                    else:
                        total_failed  += 1

                tool_rows.append({
                    "request_index":    req_idx,
                    "round_index":      round_idx,
                    "tool_name":        tc_name,
                    "tool_call_id":     tc_id,
                    "is_mcp_tool":      is_mcp,
                    "retry_count":      retry,
                    "success":          success,
                    "error_msg":        result_text[:200] if not success else "",
                    "response_preview": response_preview,
                })

        # ── tool calls from raw response items (older / GPT export format)
        for resp_item in req.get("response", []):
            if not isinstance(resp_item, dict):
                continue
            if resp_item.get("kind") == "toolInvocationSerialized":
                rd = resp_item.get("resultDetails", {})
                if not isinstance(rd, dict):
                    rd = {}
                if rd.get("isError"):
                    # Count the error; the tool was already not counted above
                    # so only add here if NOT already covered by toolCallRounds
                    pass  # avoid double-counting; toolCallRounds is authoritative

    # ── build the single summary row ────────────────────────────────────────
    n_requests = len(requests)

    def ts_utc(ms):
        if ms is None:
            return ""
        try:
            return datetime.fromtimestamp(ms / 1000.0, tz=timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S UTC"
            )
        except Exception:
            return str(ms)

    ts_start = min(timestamps) if timestamps else None
    ts_end   = max(timestamps) if timestamps else None

    success_rate = (
        round(100.0 * total_success / total_tool_calls, 1)
        if total_tool_calls > 0 else ""
    )

    summary = {
        "model":                       Path(chat_path).resolve().parts[-3]
                                       if len(Path(chat_path).resolve().parts) >= 3
                                       else "UnknownModel",
        "scenario":                    Path(chat_path).resolve().parts[-2]
                                       if len(Path(chat_path).resolve().parts) >= 2
                                       else "UnknownScenario",
        "model_id":                    model_id,
        "chat_file":                   chat_path,
        "has_token_counts":            has_token_counts,
        "timestamp_start_utc":         ts_utc(ts_start),
        "timestamp_end_utc":           ts_utc(ts_end),
        "total_wall_time_s":           round(total_elapsed_ms / 1000.0, 1) if has_elapsed else "",
        "total_requests":              n_requests,
        "n_human_interventions":       max(n_requests - 1, 0),
        "n_max_tools_exceeded":            n_max_exceeded,
        "total_mcp_tool_calls":           total_tool_calls,
        "total_mcp_tool_calls_success":   total_success,
        "total_mcp_tool_calls_failed":    total_failed,
        "mcp_tool_success_rate_pct":      success_rate,
        "total_mcp_retries":              total_retries,
        "total_prompt_tokens":         total_prompt_tokens if has_token_counts else "",
        "total_completion_tokens":     total_completion_tokens if has_token_counts else "",
        "total_tokens":                (total_prompt_tokens + total_completion_tokens)
                                       if has_token_counts else "",
    }
    return summary, tool_rows


def write_csv(rows, filepath: str, fieldnames: list = None):
    # Accept a single dict (summary) or a list of dicts
    if isinstance(rows, dict):
        rows = [rows]
    if not rows:
        print(f"  (no data to write for {filepath})")
        return
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  Written: {filepath}  ({len(rows)} row{'s' if len(rows) != 1 else ''})")


# ---------------------------------------------------------------------------
# entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) != 2:
        print("Usage: python metrics_extractor.py <chat_file.json>")
        sys.exit(1)

    chat_path = sys.argv[1]
    if not os.path.exists(chat_path):
        print(f"Error: file not found: {chat_path}")
        sys.exit(1)

    with open(chat_path, "r", encoding="utf-8") as f:
        try:
            chat_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: invalid JSON – {e}")
            sys.exit(1)

    model, scenario = parse_model_scenario(chat_path)
    prefix  = f"{model}_{scenario}"
    out_dir = os.path.dirname(os.path.abspath(chat_path))

    summary, tool_rows = extract_metrics(chat_data, chat_path)

    summary_csv = os.path.join(out_dir, f"{prefix}_chat_summary.csv")
    tool_csv    = os.path.join(out_dir, f"{prefix}_tool_metrics.csv")

    summary_fields = [
        "model", "scenario", "model_id", "chat_file", "has_token_counts",
        "timestamp_start_utc", "timestamp_end_utc", "total_wall_time_s",
        "total_requests", "n_human_interventions", "n_max_tools_exceeded",
        "total_mcp_tool_calls", "total_mcp_tool_calls_success", "total_mcp_tool_calls_failed",
        "mcp_tool_success_rate_pct", "total_mcp_retries",
        "total_prompt_tokens", "total_completion_tokens", "total_tokens",
    ]
    tool_fields = [
        "request_index", "round_index", "tool_name", "tool_call_id",
        "is_mcp_tool", "retry_count", "success", "error_msg", "response_preview",
    ]

    # ── print summary ────────────────────────────────────────────────────────
    s = summary
    deprecated_note = "  ⚠ token counts not available (old client – deprecated)" \
                      if not s["has_token_counts"] else ""
    print(f"\nModel    : {s['model']}  ({s['model_id']})")
    print(f"Scenario : {s['scenario']}")
    print(f"Requests : {s['total_requests']}  "
          f"(human interventions: {s['n_human_interventions']}, "
          f"max-tools-exceeded: {s['n_max_tools_exceeded']})")
    print(f"MCP tools: {s['total_mcp_tool_calls_success']} ok / "
          f"{s['total_mcp_tool_calls_failed']} failed / "
          f"{s['total_mcp_tool_calls']} total  "
          f"({s['mcp_tool_success_rate_pct']}% success)  "
          f"retries: {s['total_mcp_retries']}")
    if has_wall := s["total_wall_time_s"]:
        print(f"Wall time: {has_wall} s")
    print(f"Tokens   : {s['total_tokens'] or 'N/A'}{deprecated_note}")

    write_csv(summary,   summary_csv, summary_fields)
    write_csv(tool_rows, tool_csv,    tool_fields)

    print("\nNote: temperature/seed/prompt-version are not stored in the export.")
    print("      Compute cost = token counts × per-model pricing (applied externally).")


if __name__ == "__main__":
    main()
