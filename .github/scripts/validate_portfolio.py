from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
errors: list[str] = []

for markdown in ROOT.rglob("*.md"):
    text = markdown.read_text(encoding="utf-8", errors="replace")
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().split(" ", 1)[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = unquote(target.split("#", 1)[0])
        if local and not (markdown.parent / local).resolve().exists():
            errors.append(f"Broken link in {markdown.relative_to(ROOT)}: {target}")

pine_files = list(ROOT.rglob("*.pine"))
for pine in pine_files:
    text = pine.read_text(encoding="utf-8", errors="replace")
    if not re.search(r"^//@version=\d+", text, re.MULTILINE):
        errors.append(f"Missing Pine version: {pine.relative_to(ROOT)}")
    if not re.search(r"\b(indicator|strategy|library)\s*\(", text):
        errors.append(f"Missing Pine declaration: {pine.relative_to(ROOT)}")

if errors:
    print("\n".join(errors))
    raise SystemExit(1)

print(f"Validated {len(pine_files)} Pine files and local Markdown links.")
