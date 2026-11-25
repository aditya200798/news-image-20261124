#!/usr/bin/env python3
"""news-image-20261124 entry: writes one image summing up Tuesday 24 November 2026.

The image (entry.png, drawn for this entry) is held in the repository and this
program copies it byte-for-byte to the output, so both grader runs produce
identical bytes. Standard library only; no network.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import hashlib
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
dest = out_dir / "entry.png"
shutil.copyfile(src, dest)

# Fail loudly rather than emit a truncated image if the copy ever diverges.
if hashlib.sha256(dest.read_bytes()).digest() != hashlib.sha256(src.read_bytes()).digest():
    raise SystemExit("copy verification failed: output differs from entry.png")
