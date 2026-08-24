# Pull Request

## Summary

Describe what this pull request changes and why.

## Change type

- [ ] Pine Script indicator logic
- [ ] Bug fix
- [ ] Documentation
- [ ] Test / validation
- [ ] Screenshot / visual evidence
- [ ] Repository maintenance

## Validation performed

For Pine Script or behavior-related changes, record the checks completed:

- [ ] Script compiles in TradingView
- [ ] Script renders without runtime errors
- [ ] Tested on relevant EGX symbols
- [ ] Tested on relevant timeframes
- [ ] Live-bar vs bar-close behavior reviewed where applicable
- [ ] Alerts reviewed where applicable
- [ ] Stateful objects / tables / labels checked for stability
- [ ] Screenshots or evidence updated if behavior changed
- [ ] `python3 scripts/validate_repo.py` passes locally

## TradingView test evidence

List the symbols, timeframes, and evidence used for validation.

Example:

- Symbol: `EGX:COMI`
- Timeframe: `15m`
- Result: Pass
- Screenshot: `screenshots/...`

## Risk / regression notes

Describe any known limitations, repainting or timing considerations, higher-timeframe behavior, or areas that need extra review.

## Checklist

- [ ] No secrets, tokens, or credentials are included
- [ ] Documentation matches the implemented behavior
- [ ] Relative Markdown links are valid
- [ ] File naming follows repository conventions
- [ ] No unrelated files were changed
- [ ] Trading-performance claims are not inferred from software validation alone
