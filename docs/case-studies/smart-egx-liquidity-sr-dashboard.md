# Case Study — Smart EGX Liquidity S/R Dashboard

## Goal

Document the engineering behavior, validation scope, and known limitations of the **Smart EGX Liquidity S/R Dashboard** portfolio indicator without making claims about trading profitability.

## Project context

- **Language:** Pine Script v6
- **Status:** Beta
- **Category:** Smart Money / Structure / Liquidity
- **Portfolio role:** Demonstrate a multi-module TradingView overlay that combines market structure, supply/demand zones, liquidity-sweep detection, trend/momentum context, a compact dashboard, and alert conditions.

## Core components

The script combines several rule-based modules:

1. **Supply and demand zones** generated from confirmed pivot highs/lows.
2. **BOS / CHOCH structure logic** derived from breaks of confirmed pivot levels.
3. **Liquidity sweep detection** using wick/body ratios and recent range extremes.
4. **Volume-spike context** using a configurable moving-average multiplier.
5. **Trend and momentum context** using EMA, RSI, ADX, and optional EGX EMA pack overlays.
6. **Composite market-bias score** that aggregates directional conditions into Bullish / Bearish / Neutral states.
7. **Dashboard output** for nearest resistance, nearest support, last break, bias, and active levels.
8. **TradingView alert conditions** for BOS, CHOCH, liquidity sweeps, and trap-style events.

## Engineering design notes

### Confirmed pivots instead of immediate swing guesses

The zone and structure engine uses `ta.pivothigh()` and `ta.pivotlow()` with a configurable `pivotLen`. This means a pivot becomes known only after the required right-side bars are available.

**Implication:** the design intentionally trades immediacy for confirmation. Historical pivots should not be interpreted as signals that were available on the original pivot bar.

### Managed chart objects

Supply and demand zones are stored in arrays and trimmed to the configured `maxActiveZones` value. Older boxes are deleted when the active-zone limit is exceeded.

This reduces chart-object accumulation and keeps the script within TradingView object limits during extended use.

### Zone separation

Before adding a new zone, the script checks percentage distance from existing zones. This prevents clusters of nearly identical levels from being added repeatedly.

### Explicit broken-zone state

Each zone has an associated Boolean state indicating whether price has broken it. The script marks the state when price closes beyond the corresponding zone boundary.

### Dashboard architecture

The dashboard is updated on `barstate.islast`, keeping table rendering focused on the latest visible state rather than rebuilding unnecessary historical table states.

## Validation evidence

The portfolio copy was compiled and visually checked successfully in TradingView before publication.

**Validation chart:** `EGX:RMDA` · 1D  
**Validation date:** 2026-08-21

![Smart EGX Liquidity S/R Dashboard](../../screenshots/01-smart-egx-liquidity-dashboard.png)

Source: [`indicators/01-smart-egx-liquidity-sr-dashboard.pine`](../../indicators/01-smart-egx-liquidity-sr-dashboard.pine)

## What the validation proves

The validation supports the following limited technical claims:

- The published portfolio copy compiles under Pine Script v6.
- It can be added to a TradingView chart in the tested setup.
- Supply/demand objects, labels, shapes, dashboard elements, and plotted overlays can render together.
- The script exposes the expected alert-condition hooks.

## What the validation does **not** prove

The validation does not establish:

- profitability;
- predictive accuracy;
- robustness across all EGX symbols or timeframes;
- absence of false signals;
- suitability for live trading without additional testing;
- statistically significant edge.

## Repainting / timing considerations

### Pivot confirmation delay

Because pivots require right-side confirmation bars, pivot-derived zones and structure references are delayed by design.

### Live-bar variability

Conditions such as crossovers, wick ratios, volume spikes, liquidity sweeps, and composite score inputs may change before the current bar closes.

For operational use, alerts and signal interpretation should be evaluated with explicit bar-close rules where appropriate.

## Risk and quality considerations

- A composite score can simplify interpretation, but it can also hide disagreement among underlying signals.
- Market-structure labels are rule-based approximations rather than institutional order-flow data.
- Supply/demand zones are derived from pivots and ATR-based thickness, so their usefulness depends on symbol volatility and timeframe.
- Trap-style conditions are heuristic definitions, not proof of manipulative activity.
- The script should be tested across multiple EGX symbols and regimes before any practical deployment.

## Recommended next validation steps

1. Run the indicator on a representative basket of liquid EGX symbols.
2. Compare behavior across 15m, 1h, 4h, and 1D timeframes.
3. Record frequency and follow-through of BOS / CHOCH events.
4. Quantify liquidity-sweep false-positive rates.
5. Compare bar-close alerts with intrabar observations.
6. Measure chart-object stability during long historical ranges.
7. Build reproducible case studies from predefined test windows rather than visually selected examples.

## Conclusion

This indicator is best treated as a **multi-factor technical-analysis dashboard prototype** rather than a proven trading system. Its current portfolio value is strongest as evidence of Pine Script v6 development, state management, chart-object handling, market-structure logic, dashboard design, and transparent documentation of limitations.

---

This case study is for software demonstration, technical research, and education only. It is not financial advice.
