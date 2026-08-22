# Pine Script Portfolio — Engineering Case Studies

This directory contains technical case studies for every indicator in the curated Pine Script v6 portfolio.

The case studies focus on implementation architecture, validation evidence, timing behavior, repainting/confirmation considerations, and known limitations. They do **not** claim trading profitability or predictive accuracy.

## Case study index

### 1. Smart EGX Liquidity S/R Dashboard

Focus: confirmed pivots, supply/demand zone state, BOS/CHOCH logic, liquidity sweeps, chart-object management, dashboard rendering, and alerts.

[Read case study](smart-egx-liquidity-sr-dashboard.md)

### 2. AboSamra Pro

Focus: four-EMA trend structure, RSI momentum classification, manual support/resistance context, bilingual dashboard design, and alert behavior.

[Read case study](05-abosamra-pro.md)

### 3. EGX Smart Balance Matrix Pro

Focus: modular trend/momentum/liquidity engines, confirmed structure pivots, weighted rule-based scoring, threshold-cross signals, and dashboard architecture.

[Read case study](02-egx-smart-balance-matrix-pro.md)

### 4. Smart Correction Signals Pro

Focus: EMA trend context, RSI/MACD/Bollinger confirmation, confirmed swing anchors, Fibonacci correction zones, and timing limitations.

[Read case study](smart-correction-signals-pro.md)

### 5. EGX Pro Price Matrix

Focus: confirmed prior-day OHLC data, daily pivot matrix levels, EMA/volume context, label state management, dashboard logic, and live-bar signal behavior.

[Read case study](04-egx-pro-price-matrix.md)

## Validation scope

The five portfolio indicators compiled successfully and passed the documented visual chart checks on the portfolio validation setup. Those checks establish technical compatibility and observable rendering behavior only.

For the broader archive and the separate 120-script TradingView validation project, see:

[`Alaamo7/pine-script-indicators`](https://github.com/Alaamo7/pine-script-indicators)

## Engineering principle

The portfolio separates three different claims:

1. **The code compiles.**
2. **The indicator renders and behaves as documented on the tested chart.**
3. **The trading logic is profitable or robust.**

Only the first two are supported by the current portfolio validation evidence. The third requires separate strategy/backtest and out-of-sample evidence.
