# Core Papers Map

| Paper | Workstream | Why it matters in this repo |
| --- | --- | --- |
| Giannone, Reichlin, Small (2008) | `model`, `evaluation` | Defines real-time nowcast updating under asynchronous data arrival and ragged-edge panels. |
| Mariano, Murasawa (2003) | `model` | Provides the monthly-to-quarterly aggregation logic behind quarterly GDP linkage. |
| Banbura, Modugno (2014) | `model` | Main reference for EM/Kalman handling of missing patterns in factor models. |
| Croushore, Stark (2001) | `data`, `evaluation` | Motivates exact vintage usage and RTDSM handling discipline. |
| Croushore, Stark (2003) | `evaluation` | Supports the importance of vintage-consistent forecast evaluation. |
| Koenig, Dolmas, Piger (2003) | `data`, `evaluation` | Clarifies why current-vintage backfills are not valid real-time substitutes. |
| Jacobs, van Norden (2011) | `extension` | Guides the revision-aware state logic and revision measurement interpretation. |
| Anesti, Galvao, Miranda-Agrippino (2022) | `positioning`, `extension` | Closest paper for GDP revision-aware nowcasting and output design. |
| Aruoba et al. (2016) | `future_extension` | GDP/GDI upgrade path only, not part of v1 implementation. |

## Reading order

1. `Croushore, Stark (2001)`
2. `Giannone, Reichlin, Small (2008)`
3. `Banbura, Modugno (2014)`
4. `Mariano, Murasawa (2003)`
5. `Jacobs, van Norden (2011)`
6. `Anesti, Galvao, Miranda-Agrippino (2022)`
