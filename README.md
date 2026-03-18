# Supplementary Material Organization

This repository contains the supplementary material for the MCP servers paper on multiscale modeling.

The active analysis content has been updated to the latest rerun and reorganized for easier navigation.

## Active Analysis Content

- `Gpt_5/`
- `Gpt_o4_mini/`
- `Sonnet_4/`

These folders are now the main scenario outputs used by the notebooks.

## Notebooks

The original monolithic notebook was split into four notebooks:

- `Scenario_1_analysis.ipynb`
- `Scenario_2_analysis.ipynb`
- `Scenario_3_analysis.ipynb`
- `LLM_performance_metrics_analysis.ipynb`

For backward compatibility, `Scenarios_analysis.ipynb` is still present and its paths were updated to match the new folder layout.

## Outputs

Generated artifacts are grouped under `outputs/`:

- `outputs/figures/`: PNG/PDF figures
- `outputs/tables/`: LaTeX tables
- `outputs/metrics/`: CSV metric exports

Notebook save paths were updated so newly generated files are written into these folders.

## Deprecated Content

Previous analysis snapshots are archived under `deprecated/`:

- `deprecated/Sonnet4/`
- `deprecated/gpt_5/`
- `deprecated/gpt_o4_mini/`
- `deprecated/updated_MCP_container/`
- `deprecated/Scenarios_analysis_full.ipynb`

This ensures no prior analysis is lost while keeping the main workspace focused on the latest results.

## Notes

- Relative paths in the active notebooks now target `Gpt_5/`, `Gpt_o4_mini/`, and `Sonnet_4/` directly.
- The LLM metrics notebook was adjusted to run standalone from a fresh kernel (no hidden variable dependencies).
