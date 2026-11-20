"""Front page for Friday 20 November 2026 (news-image-20261120).

A tiny stdlib-only entrypoint. The artwork itself is baked at build time by
render_v1.py and stored next to this script as entry.png; this file just
places that image where the harness expects it, so every run yields the
exact same bytes and no network is ever touched.

Usage:
    python3 main.py [DEST_DIR]

DEST_DIR defaults to $MAKEFUN_OUTPUT_DIR, falling back to /output.
"""

import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGE = ROOT / "entry.png"


def resolve_dest(argv):
    if len(argv) > 1:
        return Path(argv[1])
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def run(argv):
    dest = resolve_dest(argv)
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, dest / "entry.png")


if __name__ == "__main__":
    run(sys.argv)
