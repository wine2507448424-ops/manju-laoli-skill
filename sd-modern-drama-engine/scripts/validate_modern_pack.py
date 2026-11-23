#!/usr/bin/env python3
"""Lightweight structural validator for the Modern Drama Director add-on."""
from pathlib import Path
import sys

REQUIRED = [
    "SKILL.md",
    "references/visual-mode-bible.md",
    "references/modern-location-library.md",
    "references/space-and-blocking-template.md",
    "references/camera-coverage-template.md",
    "references/continuity-ledger.md",
    "templates/scene-pack.md",
    "templates/shot-pack.md",
]

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    missing = [p for p in REQUIRED if not (root / p).is_file()]
    if missing:
        print("FAIL: missing files:")
        for p in missing:
            print(" -", p)
        return 1
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    for token in ("LIVE_ACTION", "3D_CG", "blocking-direction.md", "M0/M1/M2"):
        if token not in skill:
            print("FAIL: required contract missing:", token)
            return 1
    print("PASS: Modern Drama Director add-on structure is complete.")
    print("NOTE: This is a structural check only; it does not replace the original package QC.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
