"""Resize assets/source.png to 1024x1024 and save it as assets/entry.png.

The output is JPEG data (the filename stays entry.png), with quality lowered
from 95 toward 70 until the file is at most 1,000,000 bytes. Prints the size.
"""
from PIL import Image
import io, os

img = Image.open("assets/source.png").convert("RGB").resize((1024, 1024), Image.LANCZOS)
for q in range(95, 65, -5):
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=q)
    if buf.tell() <= 1_000_000 or q == 70:
        break
with open("assets/entry.png", "wb") as f:
    f.write(buf.getvalue())
print(os.path.getsize("assets/entry.png"))
