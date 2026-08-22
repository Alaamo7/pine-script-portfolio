# Case Study: EGX Smart Balance Matrix Pro

## Objective

Build a compact Pine Script v6 dashboard that combines multiple independent technical-analysis dimensions into one interpretable EGX-oriented decision matrix.

The emphasis of this case study is software design and signal composition, not claims of trading profitability.

## Source and visual evidence

- Source: [`indicators/03-egx-smart-balance-matrix-pro.pine`](../../indicators/03-egx-smart-balance-matrix-pro.pine)
- Portfolio screenshot: [`screenshots/03-egx-smart-balance-matrix.png`](../../screenshots/03-egx-smart-balance-matrix.png)
- Portfolio status: Active Beta
- Validation status: compiled successfully and received a visual chart check during portfolio validation.

## Architecture

The indicator is split into several analytical engines and then combines them through a weighted score.

### 1. Trend engine

The trend layer uses a configurable fast and slow EMA.

- Bullish trend: price above fast EMA and fast EMA above slow EMA.
- Bearish trend: price below fast EMA and fast EMA below slow EMA.
- Trend contributes a comparatively large weight of `+2` or `-2` to the composite score.

This intentionally gives the broader directional filter more influence than a single momentum or volume event.

### 2. Momentum engine

Momentum requires agreement between RSI and MACD:

- Bullish momentum: RSI above 50 and MACD line above signal line.
- Bearish momentum: RSI below 50 and MACD line below signal line.

Momentum contributes `+1` or `-1`.

Using two conditions reduces the chance that one oscillator alone determines the dashboard state.

### 3. Volume and liquidity context

Volume is compared with a moving average multiplied by a configurable spike factor.

A high-volume bullish candle is presented as `Inflows`; a high-volume bearish candle as `Outflows`; otherwise the state is `Normal`.

This module contributes `+1` or `-1` when a qualifying spike exists.

The labels are heuristic descriptions of candle/volume behavior; they are not order-flow measurements from an exchange feed.

### 4. SMC-lite structure engine

The script tracks confirmed pivot highs and lows using `ta.pivothigh()` and `ta.pivotlow()`.

It derives:

- bullish and bearish Break of Structure events,
- high and low liquidity-sweep candidates,
- wick/body conditions,
- volume confirmation for sweep candidates.

A sweep carries a larger score weight (`+2` or `-2`) while a BOS contributes `+1` or `-1`.

## Weighted decision model

The score combines:

| Component | Bullish weight | Bearish weight |
|---|---:|---:|
| Trend | +2 | -2 |
| Momentum | +1 | -1 |
| Volume context | +1 | -1 |
| Liquidity sweep | +2 | -2 |
| Break of Structure | +1 | -1 |

The resulting state is mapped to five dashboard labels:

- `Strong Buy` for score >= 4
- `Accumulation / Bullish` for score >= 2
- `Neutral / Wait` between those thresholds
- `Distribution / Bearish` for score <= -2
- `Strong Sell` for score <= -4

The names are interface labels for rule-based technical states. They are not brokerage recommendations.

## Signal generation

The script creates discrete chart signals when the composite score crosses important thresholds:

- Buy signal: score crosses above 3.
- Sell signal: score crosses below -3.

This is different from simply checking whether the score is currently high or low: a crossing represents a state transition.

Alerts are also exposed for score transitions, BOS events, and liquidity sweeps.

## Balance pivot layer

A separate price-reference layer computes classic pivot values from the previous bar:

- Pivot
- R1 / R2
- S1 / S2

These are displayed in the dashboard alongside the analytical score, allowing price-reference levels and multi-factor state to coexist without mixing their calculations.

## Dashboard design

The table exposes eleven rows of information including:

- symbol,
- two upper reference levels,
- pivot,
- two lower reference levels,
- liquidity state,
- momentum state,
- structure state,
- numeric score,
- final decision label.

The dashboard position is configurable between top-right, middle-right, and bottom-right.

This design turns several internal calculations into one inspection surface rather than forcing a user to infer the state from many independent plots.

## Repainting and timing considerations

The structure layer uses confirmed pivots. A pivot is only known after the configured number of right-side bars has elapsed.

Therefore:

- historical pivot-derived structure is intentionally delayed by confirmation,
- BOS and sweep logic depend on the most recently confirmed swing levels,
- the current composite score can change intrabar as price and volume change,
- current-bar signal conditions should be evaluated with the intended bar-close workflow before practical use.

This behavior is documented as a timing characteristic rather than hidden as a perfect real-time signal.

## What validation proves

The portfolio validation establishes that this Pine v6 copy:

- compiled successfully in TradingView,
- loaded on the validation chart,
- produced its intended visual dashboard for inspection.

It does not establish:

- profitability,
- robustness across all EGX symbols,
- robustness across market regimes,
- optimal score weights,
- absence of false signals.

## Engineering value

This project demonstrates several useful Pine Script design patterns:

1. decomposing technical analysis into independent modules,
2. combining Boolean states through explicit weighted scoring,
3. separating score computation from dashboard presentation,
4. using confirmed pivots for structure-aware logic,
5. exposing state transitions through `alertcondition()`,
6. documenting the difference between technical validation and strategy performance.

## Recommended next validation steps

- Test the score distribution across multiple EGX symbols and timeframes.
- Measure how often each score band occurs.
- Compare threshold-cross signals against a defined forward-return framework.
- Test alternative component weights without selecting them only from favorable historical results.
- Separate bar-close and intrabar observations.
- Document representative false-positive and neutral cases as well as visually successful setups.

## Conclusion

EGX Smart Balance Matrix Pro is best understood as a rule-based decision-dashboard prototype. Its main portfolio value is the architecture: several interpretable technical modules are combined into a transparent score and presented in a compact TradingView interface while known confirmation and validation limits remain explicit.
