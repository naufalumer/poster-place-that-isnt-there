#!/usr/bin/env python3
"""AERION poster entry: copy the pre-rendered poster to the output dir.

The poster is a hand-painted Studio Ghibli style travel poster for a
floating island that does not exist. It is rendered once, committed as
entry.png beside this script, and this program only copies it to the
directory make.fun grades (MAKEFUN_OUTPUT_DIR, default /output).
Standard library only: the grading image has no Pillow and no fonts.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print("entry.png is missing next to main.py", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"copied {SOURCE} ({target.stat().st_size} bytes) to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
