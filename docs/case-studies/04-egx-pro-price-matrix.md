# Engineering Case Study — EGX Pro Price Matrix

## Overview

`EGX Pro Price Matrix v1.0` is a Pine Script v6 indicator that combines a prior-day daily pivot matrix with EMA trend context, volume context, right-side price labels, a compact dashboard, and simple pivot-cross entry/exit signals.

This case study documents implementation behavior and validation limits. It does **not** claim trading profitability or predictive accuracy.

## Design goals

The script is designed to answer a compact set of chart-review questions:

1. What are the prior-day pivot-derived reference levels?
2. Is price currently above or below the daily pivot?
3. Is the shorter EMA above or below the longer EMA?
4. Is current volume above its moving average?
5. Has price crossed the daily pivot while aligned with the fast EMA?

## 1. Prior-day daily data

The indicator retrieves the previous completed daily bar using `request.security()`:

- previous daily high
- previous daily low
- previous daily close

The calls use `barmerge.lookahead_off`, and the source values are explicitly indexed with `[1]`. This means the matrix is anchored to the prior completed daily session rather than the still-forming current daily candle.

This is an important engineering property because it avoids using future daily values for the matrix calculation.

## 2. Pivot matrix

From the prior-day OHLC values, the script calculates a classic pivot structure:

- Pivot
- R1 / R2 / R3
- S1 / S2 / S3

The script also derives three additional presentation levels:

- `Golden Target 1`
- `Golden Target 2`
- `Transformation`

These extra labels are repository-specific derived reference levels. Their names are UI labels, not validated price forecasts.

## 3. Trend and liquidity context

Two moving averages provide simple trend context:

- EMA 50 — labelled as the liquidity EMA
- EMA 200 — main trend EMA

The dashboard classifies trend as bullish when EMA 50 is above EMA 200, otherwise bearish.

Volume context is intentionally simple:

- 20-period moving average of volume by default
- `High` liquidity state when current volume exceeds that moving average
- otherwise `Calm`

This is a descriptive volume filter, not an order-flow or institutional-liquidity model.

## 4. Entry and exit signal logic

The script defines two event signals:

### Entry

A buy/entry event occurs when:

- price crosses **above** the daily pivot, and
- price is above EMA 50.

### Exit

A sell/exit event occurs when:

- price crosses **below** the daily pivot, and
- price is below EMA 50.

Because `ta.crossover()` and `ta.crossunder()` are evaluated on live chart updates, current-bar conditions can change before the bar closes.

The labels `IN` and `OUT` should therefore be understood as rule-based chart events, not guaranteed trade instructions.

## 5. Label management

Instead of continuously creating new labels for every bar, the script keeps persistent references for each matrix level and updates their coordinates and text on the last bar.

This provides two benefits:

- lower visual clutter
- bounded object creation compared with repeatedly generating duplicate labels

The right-side label offset is user-configurable.

## 6. Dashboard architecture

A compact four-row table summarizes:

- Market State — price relative to pivot
- Liquidity — current volume relative to its moving average
- Trend — EMA 50 relative to EMA 200
- Symbol

The dashboard is rendered on `barstate.islast`, keeping it focused on the current chart state rather than historical table instances.

## 7. Alert hooks

The indicator exposes alert conditions for:

- pivot-cross entry
- pivot-cross exit

These alerts reuse the same rule-based signal conditions displayed on the chart.

## Validation status

The portfolio copy was compiled successfully in Pine Script v6 and visually checked on TradingView during the portfolio validation run.

Portfolio validation context:

- Symbol used for screenshot validation: `EGX:RMDA`
- Timeframe: `1D`
- Screenshot date: 2026-08-21
- Compile check: Passed
- Visual chart check: Passed

Screenshot: [`../../screenshots/05-egx-pro-price-matrix.png`](../../screenshots/05-egx-pro-price-matrix.png)

Source: [`../../indicators/05-egx-pro-price-matrix.pine`](../../indicators/05-egx-pro-price-matrix.pine)

## Repainting and timing considerations

The daily reference matrix is comparatively stable because it uses prior-day OHLC data with `lookahead_off`.

However:

- entry/exit events depend on the current chart bar
- EMA values change with the current bar
- volume classification changes as current-bar volume updates
- therefore live-bar signals and dashboard states may change before close

This distinction is important: **stable reference levels do not make all current-bar signals immutable.**

## What this validation proves

The documented validation supports that the portfolio copy:

- compiles under Pine Script v6
- renders on the tested TradingView chart
- displays its matrix, labels, dashboard, and signal logic without a compilation failure in that test

## What this validation does not prove

It does not establish:

- profitability
- predictive accuracy
- optimal EMA or volume settings
- suitability across all EGX instruments or timeframes
- execution quality, slippage, or brokerage costs
- statistical edge of pivot-cross events

## Recommended next validation steps

A stronger research phase would include:

1. Test the matrix on multiple EGX symbols and intraday/daily timeframes.
2. Measure how often pivot-cross signals reverse before bar close.
3. Compare bar-close-only alerts with intrabar alerts.
4. Evaluate signal outcomes separately for bullish and bearish EMA regimes.
5. Convert the event rules into a dedicated strategy prototype if performance testing is required.
6. Record sample size, transaction-cost assumptions, drawdown, and out-of-sample results before making any performance claim.

## Engineering takeaway

The strongest aspect of this indicator is not a prediction claim. It is the separation of:

- **stable prior-session reference data**,
- **current trend and volume context**,
- **event-driven pivot-cross signals**, and
- **presentation/state management**.

That makes the script useful as a clear example of a multi-timeframe Pine Script dashboard while keeping the limitations of live-bar signals explicit.
