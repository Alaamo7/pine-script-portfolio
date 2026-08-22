# Contributing

This repository is a curated technical portfolio. Changes should preserve traceability between source code, validation evidence, screenshots, case studies, and documentation.

## Change workflow

1. Open an issue for a bug, documentation gap, validation concern, or proposed enhancement.
2. Create a focused branch for one change.
3. Keep code changes, screenshots, and documentation synchronized.
4. Re-test the affected Pine Script in TradingView when source logic changes.
5. Update the relevant case study or verification notes when behavior changes.
6. Update `CHANGELOG.md` for user-visible changes.
7. Open a pull request describing what changed, why, and how it was verified.

## Validation expectations

For Pine Script changes, record:

- TradingView compile result.
- Symbol and timeframe used for the visual check.
- Whether the change affects live-bar behavior, pivot confirmation, higher-timeframe data, or alert timing.
- Screenshot evidence when the visible output changes.
- Any known limitation or unresolved edge case.

A successful compile does not establish profitability, robustness, or predictive accuracy.

## Scope

Good contributions include documentation fixes, reproducible bug fixes, clearer validation evidence, maintainability improvements, and carefully reviewed indicator refinements.

Do not submit changes that add unsupported performance claims, remove documented limitations, or present rule-based outputs as AI predictions.

## Licensing

Review `LICENSE.md` before contributing or reusing repository content. Contributions do not override the repository's stated usage restrictions.
