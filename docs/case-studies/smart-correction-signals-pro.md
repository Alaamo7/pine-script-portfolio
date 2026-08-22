# Case Study — Smart Correction Signals Pro

## Objective

Document the engineering behavior of **Smart Correction Signals Pro v1.0**, a Pine Script v6 indicator designed to identify potential correction setups by combining trend direction, momentum, volatility, confirmed swing structure, and Fibonacci retracement zones.

This case study describes implementation logic and validation scope. It does **not** claim trading profitability or predictive accuracy.

## Source and validation context

- Repository: `Alaamo7/pine-script-portfolio`
- Script: `indicators/04-smart-correction-signals-pro.pine`
- Portfolio status: Beta
- Portfolio validation: compiled successfully and received a visual TradingView chart check on `EGX:RMDA` 1D during the 2026-08-21 portfolio validation run.
- Screenshot: `screenshots/04-smart-correction-signals.png`

## Architecture

The indicator is structured as a multi-layer correction detector rather than a single-condition signal generator.

### 1. Trend filter

Two configurable exponential moving averages are used:

- Fast EMA: default 20
- Slow EMA: default 50

The script defines:

- Bullish trend when `emaFast > emaSlow`
- Bearish trend when `emaFast < emaSlow`

This prevents correction setups from being evaluated without directional context.

### 2. RSI context

RSI is calculated with a configurable period, defaulting to 14.

The default thresholds are:

- Overbought: above 70
- Oversold: below 30

RSI conditions are used as optional confirmation inputs inside the correction logic rather than as standalone entry rules.

### 3. MACD confirmation

The indicator calculates a standard configurable MACD stack:

- Fast: 12
- Slow: 26
- Signal: 9

Bullish and bearish MACD crossovers are displayed and may participate in correction confirmation.

### 4. Bollinger volatility context

Bollinger Bands are calculated from:

- 20-period SMA basis
- 2.0 standard-deviation multiplier by default

The upper and lower bands contribute another possible confirmation path when price reaches an extreme relative to recent volatility.

### 5. Confirmed swing engine

Swing highs and lows use `ta.pivothigh()` and `ta.pivotlow()` with configurable left/right confirmation bars.

The default is five bars on each side.

Important consequence: a swing is **not known at the original swing bar in real time**. It becomes confirmed only after the configured right-side bars have elapsed.

The script plots confirmed swings back at their original chart position using a negative display offset. That visual placement must not be confused with earlier real-time knowledge.

### 6. Fibonacci state

The most recently confirmed high and low are stored as persistent state.

When both exist, the script derives:

- 38.2% retracement
- 50.0% retracement
- 61.8% retracement

The code uses the variable `swingRange` for the distance between confirmed swing anchors.

These levels form contextual correction zones rather than independent forecasts.

## Correction logic

### Bullish correction setup

A correction-buy setup requires all of the following high-level conditions:

1. Fast EMA is above slow EMA.
2. Price is inside the defined Fibonacci buy zone between the 50% and 61.8% retracement levels.
3. At least one confirmation condition is true:
   - RSI is oversold, or
   - MACD crosses bullish, or
   - price is at/below the lower Bollinger Band.

### Bearish correction setup

A correction-sell setup mirrors the same structure:

1. Fast EMA is below slow EMA.
2. Price is inside the defined Fibonacci sell zone between the 38.2% and 50% levels.
3. At least one confirmation condition is true:
   - RSI is overbought, or
   - MACD crosses bearish, or
   - price is at/above the upper Bollinger Band.

## Why the design is useful as an engineering example

The indicator demonstrates several Pine Script design ideas in one compact project:

- Context gating: correction conditions only operate inside a trend regime.
- Multi-signal confirmation: RSI, MACD, and Bollinger conditions are combined with OR logic rather than treated as isolated systems.
- Confirmed-state handling: swing anchors are stored only after pivot confirmation.
- Derived-level state: Fibonacci zones update from the latest confirmed swing information.
- Configurable visualization: EMA, RSI markers, MACD markers, Bollinger Bands, swings, and Fibonacci layers can be toggled independently.
- Alert integration: correction setups and MACD crosses expose TradingView alert conditions.

## Timing and repainting considerations

### Confirmed pivots are delayed by design

Because `ta.pivothigh()` and `ta.pivotlow()` require right-side bars, swing information is delayed until confirmation.

The plotted swing marker is offset backward for chart readability, but the algorithm did not know that pivot at the earlier bar.

### Fibonacci levels can change after a newly confirmed swing

The Fibonacci framework is based on the latest stored confirmed high and low. When a new pivot becomes confirmed, those anchors can update and the displayed retracement levels can therefore move.

### Current-bar conditions can fluctuate

RSI, MACD, Bollinger position, and the correction setup itself can change during an open realtime bar. Users who require stable alerts should explicitly validate bar-close behavior before practical use.

## Validation evidence

The portfolio validation established that this Pine v6 copy:

- compiled successfully,
- loaded on TradingView,
- rendered visually on the selected validation chart,
- and produced the expected chart layers without a compile-time failure.

The repository includes the associated screenshot:

`../../screenshots/04-smart-correction-signals.png`

## What this validation does not prove

The validation does not establish:

- profitability,
- win rate,
- expected return,
- robustness across EGX symbols,
- robustness across timeframes,
- optimal parameter values,
- or superiority over simpler correction models.

Those questions require separate quantitative backtesting and out-of-sample evaluation.

## Recommended next validation steps

1. Test multiple EGX equities across daily and intraday timeframes.
2. Record the correction setup only after bar close and compare it with intrabar behavior.
3. Separate tests by market regime: trending, sideways, high-volatility, and low-liquidity periods.
4. Measure setup frequency before measuring performance.
5. Define objective invalidation and exit rules before converting the indicator into a strategy.
6. Run out-of-sample tests rather than tuning parameters only on the original validation symbol.

## Engineering takeaway

The main value of this project is not the `BUY` or `SELL` label itself. It is the explicit composition of multiple independent market-context layers into a readable Pine Script workflow with known timing limitations.

That makes it suitable as a portfolio example of indicator architecture, state management, confirmed-pivot handling, configurable visual layers, and alert integration.
