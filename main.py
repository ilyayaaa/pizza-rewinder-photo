"""Copy the prepared Pizza Rewinder catalogue photo to the output directory.

Validates that assets/entry.png is JPEG data (starts with FFD8) and at most
1 MiB, then copies it as entry.png into $MAKEFUN_OUTPUT_DIR (default /output).
"""
import os, shutil, sys

SRC = "assets/entry.png"
MAX = 1048576

with open(SRC, "rb") as f:
    if f.read(2) != b"\xff\xd8":
        sys.exit(f"error: {SRC} does not start with JPEG magic bytes FFD8; run tools/prepare.py")
size = os.path.getsize(SRC)
if size > MAX:
    sys.exit(f"error: {SRC} is {size} bytes, over the {MAX} byte limit; rerun tools/prepare.py")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(SRC, os.path.join(out, "entry.png"))
