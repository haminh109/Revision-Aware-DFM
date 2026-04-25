# Appendix

## Appendix A. Frozen Result Sources

The manuscript uses only the frozen build in:

`outputs/frozen/submission_final`

The core manuscript tables are generated from the following files:

| Manuscript object | Generated file | Frozen source |
| --- | --- | --- |
| Table 1 | `paper/tables/table_1_headline_point_forecasts.md` | `outputs/frozen/submission_final/headline_point_results.csv` |
| Table 2 | `paper/tables/table_2_exact_vs_pseudo.md` | `outputs/frozen/submission_final/headline_exact_vs_pseudo.csv` |
| Table 3 | `paper/tables/table_3_revision_forecasts.md` | `outputs/frozen/submission_final/headline_revision_results.csv` |
| Table 4 | `paper/tables/table_4_robustness_winners.md` | `outputs/frozen/submission_final/headline_point_subsample_robustness.csv` and `outputs/frozen/submission_final/headline_point_scenario_robustness.csv` |
| Appendix Table A1 | `paper/tables/appendix_a_subsample_robustness_full.md` | `outputs/frozen/submission_final/headline_point_subsample_robustness.csv` |
| Appendix Table A2 | `paper/tables/appendix_a_scenario_robustness_full.md` | `outputs/frozen/submission_final/headline_point_scenario_robustness.csv` |
| Appendix Table B1 | `paper/tables/appendix_b_small_sample_dm.md` | `outputs/frozen/submission_final/headline_point_small_sample_dm.csv` |
| Appendix Table C1 | `paper/tables/appendix_c_winner_stability.md` | `outputs/frozen/submission_final/journal_winner_stability.csv` |

## Appendix B. Model Details

The autoregressive benchmark is estimated separately for each GDP release target using expanding windows. Lag length is selected from one to four lags by BIC. This benchmark is intentionally minimal and serves as the relative RMSFE anchor in the frozen evaluation files.

The bridge benchmark maps block-level monthly indicators into each quarterly GDP release target. Within-quarter missing monthly indicators are filled using univariate autoregressive nowcasts. The bridge model is important because it remains highly competitive before the advance GDP release.

The standard dynamic factor model extracts a common monthly factor from the real-time indicator panel and links the factor to quarterly GDP through a simple aggregation rule. It is estimated separately by GDP release target and therefore does not impose a joint release ladder.

The release-structured dynamic factor model uses a shared latent quarterly activity state with separate measurement equations for `A/S/T/M`. This model is designed to exploit the fact that later GDP releases are updates of earlier GDP releases rather than independent targets.

The revision-aware model adds a parsimonious latent revision component to the release-structured system. It forecasts early GDP revisions such as `DELTA_SA` and `DELTA_TS`, but it does not yet model revisions in every monthly source indicator.

## Appendix C. Robustness Interpretation

The robustness package includes pandemic exclusion, pre-GFC and post-GFC subsamples, an expanded indicator panel, and an alternative-data-choice scenario. These checks show that exact model winners change across settings. This is why the manuscript uses a model-family interpretation.

The strongest stable pattern is not "revision_dfm always wins." The stable pattern is that release-structured and revision-aware models are the relevant model family for `S/T`, while `A` is more sensitive to bridge and standard factor benchmarks.

Small-sample Diebold-Mariano p-values are reported in `paper/tables/appendix_b_small_sample_dm.md`. They should be treated as supporting diagnostics rather than as the sole basis for the paper's claim.

## Appendix D. Figures

The paper figure package is stored in `paper/figures`:

| Figure | File | Purpose |
| --- | --- | --- |
| Figure 1 | `paper/figures/nowcast_path.png` | Shows the nowcast path across release checkpoints. |
| Figure 2 | `paper/figures/forecast_update_decomposition.png` | Shows forecast-update decomposition across checkpoints. |
| Appendix Figure | `paper/figures/submission_exact_vs_pseudo_gap.png` | Visualizes exact-vs-pseudo timing gaps. |

## Appendix E. Additional Limitations and Future Work

The most important fixable limitation is official Census release timing. Replacing proxy timing with a complete historical release archive would strengthen the exact-vs-pseudo comparison.

The second fixable limitation is the absence of an indicator-revision module. A future version can add selected monthly indicator revisions after the GDP revision block is stable.

The third fixable limitation is the lack of density forecasts. Applied users care not only about point nowcasts but also about uncertainty around each release estimate. A density extension should be added only after the point-forecast release ladder is fully validated.

The fourth fixable limitation is paper formatting. The current draft is a Markdown manuscript. Before submission, it should be converted into the target journal's Word or LaTeX template, with references checked against the journal's bibliography style.
