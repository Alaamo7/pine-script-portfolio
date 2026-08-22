# Documentation Index

This directory organizes the technical documentation for the curated Pine Script v6 portfolio.

## Start here

- [Engineering case studies](case-studies/README.md) — architecture, validation scope, timing behavior, and known limitations for all five portfolio indicators.
- [Versioning and release policy](VERSIONING.md) — release numbering, readiness criteria, and the boundary between software validation and trading-performance claims.
- [Main portfolio README](../README.md) — portfolio overview, screenshots, verification summary, usage notes, and repository links.
- [Changelog](../CHANGELOG.md) — repository and documentation milestones.
- [Contribution guide](../CONTRIBUTING.md) — issue, branch, validation, documentation, and pull-request workflow.
- [License and usage notice](../LICENSE.md) — permitted and restricted use of the published source code.

## Repository validation

A lightweight local validation script is available at [`scripts/validate_repo.py`](../scripts/validate_repo.py). It checks:

- required repository and workflow documentation files;
- the expected five curated Pine indicators;
- the expected five portfolio screenshots;
- relative Markdown links that resolve inside the repository.

The same script is executed by the GitHub Actions workflow at [`.github/workflows/repository-validation.yml`](../.github/workflows/repository-validation.yml) on pushes and pull requests targeting `main`.

## Naming policy

The curated indicator filenames use a stable numeric order from `01` to `05`. Case-study filenames created during the documentation build are retained as stable public paths to avoid unnecessary link churn; the canonical indicator-to-case-study mapping is maintained in [the case-study index](case-studies/README.md).

## Documentation principles

The portfolio keeps three claims separate:

1. **Compilation** — whether a Pine Script compiles successfully.
2. **Observed chart behavior** — whether the indicator renders and behaves as documented on the tested setup.
3. **Trading performance** — whether the logic is profitable, robust, or suitable for live use.

Current portfolio evidence supports the first two only. Trading performance requires separate backtesting, out-of-sample testing, and risk evaluation.
