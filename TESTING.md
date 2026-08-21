# TradingView validation checklist

Use this checklist after every logic change and before publishing a new screenshot or release.

## Compile and load

1. Open the script in the TradingView Pine Editor.
2. Confirm that it compiles with Pine Script v6 without warnings that affect execution.
3. Add it to a standard candlestick chart.
4. Record the symbol, timeframe, session, and test date.

## Historical and live-bar behavior

1. Test with `Confirm Signals On Bar Close` enabled.
2. Observe a live bar, wait for it to close, and confirm that the plotted signal matches the alert condition.
3. Reload the chart and check that closed-bar signals remain in the same locations.
4. For pivot logic, confirm that the marker appears only after the configured right-side confirmation bars.
5. For the price matrix, inspect the transition into a new daily session and confirm that all levels still use the previous completed day.

## Coverage

Test at least:

- Three EGX symbols with different liquidity profiles.
- Daily, 60-minute, and 15-minute charts where the indicator is intended to support them.
- A period containing a trend, a range, a gap, and a volume spike.
- The minimum and maximum supported values for the most important inputs.

## Visual and resource checks

- Confirm that tables remain readable on desktop and mobile layouts.
- Confirm that broken zones stop extending and are excluded from active-level counts.
- Confirm that labels, boxes, lines, and tables stay within the script limits.
- Capture a new screenshot only after completing the checks above.

## Result record

Record the result in the pull request or release notes with:

- Script and version
- TradingView compile result
- Symbols and timeframes tested
- Live-bar/reload result
- Known limitations
- Screenshot date

