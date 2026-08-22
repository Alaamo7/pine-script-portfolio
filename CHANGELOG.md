# Changelog

This file tracks portfolio presentation, validation evidence, documentation, and repository-level improvements. It does not represent investment-performance claims.

## 2026-08-22 — Workflow and repository validation upgrade

- Added `CONTRIBUTING.md` with an issue → branch → TradingView validation → documentation → PR workflow.
- Added bug-report and documentation issue templates.
- Added a pull-request template with compile, chart, screenshot, live-bar, alert, and limitation checks.
- Added `docs/VERSIONING.md` with release-readiness criteria and a semantic-style versioning policy.
- Added `scripts/validate_repo.py` to verify required files, the curated five-indicator set, screenshots, and relative Markdown links.
- Added a GitHub Actions repository-validation workflow for pushes and pull requests targeting `main`.
- Documented the repository naming policy while retaining stable public case-study paths.
- Opened an engineering roadmap issue for deeper multi-symbol / multi-timeframe validation before the first formal tagged release.

## 2026-08-22 — Engineering documentation upgrade

- Added engineering case studies for all five curated Pine Script v6 indicators.
- Added a unified case-study index under `docs/case-studies/README.md`.
- Linked each featured indicator to its source file, screenshot, and case study.
- Documented repainting, confirmation timing, live-bar behavior, and validation limits.
- Clarified the difference between compile/render validation and trading profitability.

## 2026-08-21 — Curated portfolio publication

- Published five curated Pine Script v6 indicators focused on EGX technical analysis.
- Added one TradingView screenshot for every portfolio indicator.
- Verified **5/5** scripts compiled successfully during portfolio validation.
- Verified **5/5** scripts passed visual chart checks.
- Applied Pine v6 compatibility fixes where needed without changing the intended indicator logic.
- Added verification notes and usage guidance to the main README.
