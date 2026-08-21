# Pine Script v6 Portfolio 📈

A focused portfolio of five Pine Script v6 indicators for Egyptian Exchange (EGX) technical analysis. Every script in this repository was compiled and displayed successfully in TradingView before publication.

> **Validation chart:** EGX:RMDA · 1D · screenshots captured on 2026-08-21. Market data shown by TradingView may be delayed.

## Portfolio

### 1. Smart EGX Liquidity S/R Dashboard

Supply and demand zones, structure breaks, liquidity sweeps, traps, and a compact market dashboard.

![Smart EGX Liquidity S/R Dashboard](screenshots/01-smart-egx-liquidity-dashboard.png)

[View Pine Script](indicators/01-smart-egx-liquidity-sr-dashboard.pine)

### 2. AboSamra Pro

A bilingual trend and momentum dashboard combining EMA 9/21/50/200, RSI, signals, and manual support/resistance context.

![AboSamra Pro](screenshots/02-abosamra-pro.png)

[View Pine Script](indicators/02-abosamra-pro.pine)

### 3. EGX Smart Balance Matrix Pro

A multi-factor EGX dashboard combining trend, momentum, liquidity, pivots, market structure, and a weighted decision score.

![EGX Smart Balance Matrix Pro](screenshots/03-egx-smart-balance-matrix.png)

[View Pine Script](indicators/03-egx-smart-balance-matrix-pro.pine)

### 4. Smart Correction Signals Pro

Correction-zone analysis using EMA, RSI, MACD, Bollinger Bands, confirmed pivots, Fibonacci levels, and configurable alerts.

![Smart Correction Signals Pro](screenshots/04-smart-correction-signals.png)

[View Pine Script](indicators/04-smart-correction-signals-pro.pine)

### 5. EGX Pro Price Matrix

A daily pivot matrix with confirmed prior-day OHLC levels, trend filters, liquidity context, entry/exit signals, and a chart dashboard.

![EGX Pro Price Matrix](screenshots/05-egx-pro-price-matrix.png)

[View Pine Script](indicators/05-egx-pro-price-matrix.pine)

## Verification status

| Indicator | Pine v6 compile | Visual chart check | Repainting notes |
|---|---:|---:|---|
| Smart EGX Liquidity S/R Dashboard | Passed | Passed | Pivots are confirmed after the configured right-side bars; live-bar conditions may fluctuate until close. |
| AboSamra Pro | Passed | Passed | No higher-timeframe requests; live-bar signals may fluctuate until close. |
| EGX Smart Balance Matrix Pro | Passed | Passed | Pivot-based structure is delayed by confirmation bars; live score may update intrabar. |
| Smart Correction Signals Pro | Passed | Passed | Fibonacci anchors use confirmed pivots; current-bar setups may change before close. |
| EGX Pro Price Matrix | Passed | Passed | Daily matrix uses prior-day OHLC values; current-bar entry/exit signals may change before close. |

## Pine v6 compatibility fixes

Two source-level compatibility fixes were applied to the portfolio copies after real TradingView compilation:

- Declared `nearestSupply` and `nearestDemand` explicitly as `float` when initialized with `na`.
- Renamed the reserved identifier `range` to `swingRange`.

The underlying indicator logic was not changed.

## Usage

1. Open a script from the `indicators/` directory.
2. Copy it into the TradingView Pine Editor.
3. Click **Add to chart**.
4. Review the inputs for the target symbol and timeframe.
5. Create alerts only after confirming the intended bar-close behavior.

## Important notes

- The scripts are presented as **Beta / Active Beta** portfolio work.
- Pivot-based signals are known only after the configured confirmation bars.
- A successful compile and visual check do not guarantee trading performance.
- Test on multiple symbols, timeframes, and market conditions before any practical use.

## Disclaimer

This repository is for education, software demonstration, and technical research only. It is not financial advice or a recommendation to buy or sell any security. Trading involves risk, and all decisions remain the user's responsibility.

## Copyright

Copyright © 2026 Alaamo7. No license is granted for redistribution, resale, or commercial use unless the owner provides written permission.
