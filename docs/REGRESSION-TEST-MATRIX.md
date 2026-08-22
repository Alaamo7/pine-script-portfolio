# Regression Test Matrix

This matrix defines the manual TradingView regression checks required before the first formal portfolio release.

## Test symbols and timeframes

Use at least three EGX symbols with different liquidity/price behavior. Minimum recommended set:

- `EGX:RMDA`
- `EGX:COMI`
- `EGX:SWDY`

Test each indicator on at least:

- `15m`
- `1D`

Where the indicator uses higher-timeframe or prior-day data, also inspect behavior around a new trading session.

## Evidence required for every test

Record:

- Indicator name
- Symbol
- Timeframe
- Test date
- Pine compile result
- Visual render result
- Screenshot path
- Live-bar observation
- Bar-close observation
- Alert behavior
- Known limitation / anomaly
- Pass / fail / needs review

Do not infer profitability from these checks.

## Cross-indicator regression matrix

| Indicator | Compile | Render | Live vs close | Alerts | Object/table stability | Pivot/HTF timing | Multi-symbol | Multi-TF |
|---|---|---|---|---|---|---|---|---|
| Smart EGX Liquidity S/R Dashboard | Required | Required | Required | Required | Zones/labels/table | Confirmed pivots | 3+ symbols | 15m + 1D |
| AboSamra Pro | Required | Required | Required | Required | S/R lines/table | N/A | 3+ symbols | 15m + 1D |
| EGX Smart Balance Matrix Pro | Required | Required | Required | Required | Table/signals | Confirmed pivots | 3+ symbols | 15m + 1D |
| Smart Correction Signals Pro | Required | Required | Required | Required | Plots/labels | Confirmed pivots/Fib anchors | 3+ symbols | 15m + 1D |
| EGX Pro Price Matrix | Required | Required | Required | Required | Labels/table | Prior-day daily OHLC | 3+ symbols | 15m + 1D |

## Indicator-specific checks

### 1. Smart EGX Liquidity S/R Dashboard

- Confirm supply/demand boxes do not exceed the configured active-zone limit.
- Confirm old boxes are deleted when trimming arrays.
- Confirm BOS/CHOCH labels appear only when their source conditions occur.
- Confirm liquidity sweep markers match wick/body and lookback conditions.
- Observe whether current-bar sweep/trap states disappear before bar close.
- Confirm dashboard updates without duplicating table objects.
- Test all alertconditions at least once when a qualifying historical/live condition can be observed.

### 2. AboSamra Pro

- Confirm EMA 9/21/50/200 hierarchy matches dashboard trend state.
- Confirm buy/sell triangles require EMA 9/21 cross plus RSI momentum class.
- Change manual support/resistance inputs and verify both lines and distance percentages update.
- Toggle support/resistance visibility and ensure old line objects are deleted.
- Observe whether cross-based signals change on the active bar before close.
- Verify trend-change alerts correspond to the documented EMA hierarchy.

### 3. EGX Smart Balance Matrix Pro

- Verify each score component separately: trend, momentum, volume, sweep, BOS.
- Confirm final score equals the visible component logic.
- Confirm threshold-cross signals only appear when score crosses +3 or -3.
- Verify decision label thresholds at ±2 and ±4.
- Observe intrabar score changes before close.
- Confirm pivot-derived BOS/sweep behavior respects pivot confirmation delay.
- Check dashboard values after symbol/timeframe changes.

### 4. Smart Correction Signals Pro

- Confirm EMA 20/50 trend state.
- Verify RSI OB/OS markers and MACD crosses independently.
- Confirm Bollinger bands render after sufficient lookback.
- Verify swing arrows are plotted back at the pivot bar using the configured right offset.
- Confirm Fibonacci levels use the last confirmed high/low pair.
- Observe whether correction setups change on the live bar.
- Test both correction alerts and MACD-cross alerts.

### 5. EGX Pro Price Matrix

- Confirm prior-day high/low/close values remain stable during the current session.
- Confirm pivot, R1-R3, S1-S3 and derived levels recompute at the next daily session.
- Verify `lookahead_off` behavior by checking that future daily values are not used.
- Confirm right-side labels are updated in place rather than duplicated each bar.
- Observe pivot-cross signals intrabar and again after bar close.
- Check high-volume state against the configured volume moving average.
- Test both entry and exit alerts.

## Pass criteria

A test case passes when:

1. The script compiles.
2. It renders without runtime errors.
3. Its visible state matches the documented rules.
4. Stateful chart objects do not accumulate unexpectedly.
5. Alerts correspond to the same conditions shown in code.
6. Any live-bar variability is documented and not presented as confirmed historical behavior.

## Failure handling

For any failure:

1. Capture a screenshot.
2. Record symbol/timeframe and exact inputs.
3. Open a GitHub issue using the bug template.
4. Classify the failure as compile, runtime, rendering, timing/repainting, alert, or documentation mismatch.
5. Fix on a branch and re-run only the affected regression cases plus at least one unaffected control case.

## Release gate

Do not create the first tagged portfolio release until:

- All five indicators pass compile/render checks across the minimum matrix.
- Live-bar vs bar-close behavior is documented for signal-producing indicators.
- No unresolved critical regression issue remains.
- Screenshots/evidence are refreshed where behavior materially changed.
- Release notes explicitly state that software validation is not profitability validation.
