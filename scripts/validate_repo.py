from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "CHANGELOG.md",
    "LICENSE.md",
    "CONTRIBUTING.md",
    "docs/README.md",
    "docs/VERSIONING.md",
    "docs/case-studies/README.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/documentation.md",
]

EXPECTED_INDICATORS = {
    "01-smart-egx-liquidity-sr-dashboard.pine",
    "02-abosamra-pro.pine",
    "03-egx-smart-balance-matrix-pro.pine",
    "04-smart-correction-signals-pro.pine",
    "05-egx-pro-price-matrix.pine",
}

EXPECTED_SCREENSHOTS = {
    "01-smart-egx-liquidity-dashboard.png",
    "02-abosamra-pro.png",
    "03-egx-smart-balance-matrix.png",
    "04-smart-correction-signals.png",
    "05-egx-pro-price-matrix.png",
}

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def check_required_paths(errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            fail(f"Missing required path: {rel}", errors)


def check_curated_sets(errors: list[str]) -> None:
    indicators_dir = ROOT / "indicators"
    screenshots_dir = ROOT / "screenshots"

    indicators = {p.name for p in indicators_dir.glob("*.pine")} if indicators_dir.exists() else set()
    screenshots = {p.name for p in screenshots_dir.glob("*.png")} if screenshots_dir.exists() else set()

    if indicators != EXPECTED_INDICATORS:
        missing = sorted(EXPECTED_INDICATORS - indicators)
        extra = sorted(indicators - EXPECTED_INDICATORS)
        if missing:
            fail(f"Missing curated indicators: {', '.join(missing)}", errors)
        if extra:
            fail(f"Unexpected curated indicators: {', '.join(extra)}", errors)

    if screenshots != EXPECTED_SCREENSHOTS:
        missing = sorted(EXPECTED_SCREENSHOTS - screenshots)
        extra = sorted(screenshots - EXPECTED_SCREENSHOTS)
        if missing:
            fail(f"Missing screenshots: {', '.join(missing)}", errors)
        if extra:
            fail(f"Unexpected screenshots: {', '.join(extra)}", errors)


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def is_external(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:", "tel:"))


def check_markdown_links(errors: list[str]) -> None:
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip()
            if not target or target.startswith("#") or is_external(target):
                continue

            target = target.split(maxsplit=1)[0].strip("<>")
            target = unquote(strip_anchor(target))
            if not target:
                continue

            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"Link escapes repository: {md.relative_to(ROOT)} -> {target}", errors)
                continue

            if not resolved.exists():
                fail(f"Broken relative link: {md.relative_to(ROOT)} -> {target}", errors)


def main() -> int:
    errors: list[str] = []
    check_required_paths(errors)
    check_curated_sets(errors)
    check_markdown_links(errors)

    if errors:
        print("Repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    print(f"Checked {len(REQUIRED_PATHS)} required paths, 5 curated indicators, 5 screenshots, and relative Markdown links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
