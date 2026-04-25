# Reproducibility Note

## Source of Truth

All manuscript numbers must come from:

`outputs/frozen/submission_final`

Do not use older output folders when editing the paper. The frozen build contains:

- `journal_results_draft.md`
- `submission_mode_report.md`
- `headline_point_results.csv`
- `headline_exact_vs_pseudo.csv`
- `headline_revision_results.csv`
- `headline_point_subsample_robustness.csv`
- `headline_point_scenario_robustness.csv`
- `headline_point_small_sample_dm.csv`
- `journal_winner_stability.csv`
- `freeze_manifest.md`
- `freeze_manifest.json`

## Generated Paper Package

The manuscript package is stored in:

`paper`

Generated tables are stored in:

`paper/tables`

Figures copied into the manuscript package are stored in:

`paper/figures`

## Evaluation Scope

The headline evaluation sample is `2005Q1-2024Q4`, with 80 quarterly forecasts in the main result files. Pandemic exclusion removes the designated pandemic quarters from robustness evaluation. Subsample checks include pre-GFC and post-GFC variants. Scenario checks include an expanded panel and an alternative-data-choice design.

The main targets are:

- `A`: advance GDP release.
- `S`: second GDP release.
- `T`: third GDP release.
- `M`: mature vintage anchor.

The main revision targets are:

- `DELTA_SA`: second release minus advance release.
- `DELTA_TS`: third release minus second release.
- `DELTA_MT`: mature vintage minus third release.

The manuscript reports `DELTA_SA` and `DELTA_TS` because those are present in the frozen headline revision results.

## Pipeline Commands

The project pipeline is designed around the following command order:

```bash
uv run radfm download-data
uv run radfm build-calendars
uv run radfm build-targets
uv run radfm build-event-panel
uv run radfm build-snapshots
uv run radfm run-benchmarks
uv run radfm run-release-dfm
uv run radfm run-revision-dfm
uv run radfm evaluate
uv run radfm build-report
```

If a command name differs in the local CLI, use the equivalent script documented in the repository. The manuscript itself should not be edited with numbers from a non-frozen rerun unless a new freeze folder is created and explicitly marked as the new source of truth.

## Traceability Rules

Every numerical claim in the manuscript should satisfy one of these rules:

- It is present directly in a frozen CSV under `outputs/frozen/submission_final`.
- It is present in a generated table under `paper/tables`, which itself states the frozen CSV source.
- It is a qualitative statement supported by `journal_results_draft.md` or `journal_winner_stability.csv`.

Do not manually type new performance numbers into the paper unless they can be traced to the frozen files.

## Known Caveats

The main data caveat is the Census timing proxy. The current build uses a first-release proxy for some Census-sensitive timing rather than a complete official historical Census archive. This caveat is disclosed in the manuscript and should remain in the submitted version unless the data layer is upgraded.

The main econometric caveat is that the revision-aware model is structural for the GDP release ladder only. It is not yet a full joint indicator-revision system.

The main interpretation caveat is that the advance GDP release is not dominated by the structured models. The manuscript should retain the conservative central claim: structured models are most useful for the second and third releases.
