# Versioning and Release Policy

This repository uses a simple semantic-style versioning policy for portfolio releases.

## Version format

`MAJOR.MINOR.PATCH`

- **MAJOR** — reserved for substantial architectural changes, incompatible portfolio structure changes, or major rewrites of the curated indicator set.
- **MINOR** — used for meaningful additions such as new validated indicators, expanded validation coverage, new engineering case studies, or major documentation/workflow improvements.
- **PATCH** — used for documentation corrections, link fixes, metadata cleanup, screenshot refreshes, or small compatibility fixes that do not materially change the trading logic.

## Release readiness checklist

A tagged release should not be created only because files changed. Before publishing a release:

1. All curated Pine files intended for the release compile in TradingView.
2. Visual chart checks are refreshed for the documented validation setup.
3. Signal-producing scripts have live-bar vs bar-close behavior documented.
4. Known repainting/confirmation limitations are recorded.
5. README, case studies, screenshots, and changelog agree with the code state.
6. Repository validation checks pass.
7. Release notes clearly separate software validation from trading-performance claims.

## First release target

The first formal tagged portfolio release should follow the broader multi-symbol / multi-timeframe validation milestone tracked in the engineering roadmap issue.

Until then, the repository may evolve on `main` as a pre-release portfolio.

## Trading-performance boundary

A software release tag means the documented code/version was packaged and technically validated to the stated scope. It does **not** certify profitability, robustness, or future trading performance.
