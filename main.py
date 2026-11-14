#!/usr/bin/env python3
"""food-picture-01-entry: write the ramen picture to the output directory.

Decodes the entry image (entry.jpg.b64, a base64 copy of the 1024x1024
JPEG of steaming tonkotsu ramen stored beside this script) and writes
it to $MAKEFUN_OUTPUT_DIR/entry.png (default /output), then validates
the written file: it must start with the JPEG magic bytes FF D8 FF and be
between 1 byte and 1 MiB. No network, no randomness, no dependencies
beyond the Python 3.13 standard library. The same bytes every run.
"""

import base64
import hashlib
import os
import sys

MAX_BYTES = 1024 * 1024
JPEG_MAGIC = b"\xff\xd8\xff"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.jpg.b64")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    with open(source, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())

    if data[:3] != JPEG_MAGIC:
        print("error: decoded image is not a JPEG", file=sys.stderr)
        return 1
    if not 1 <= len(data) <= MAX_BYTES:
        print(f"error: image size {len(data)} out of range 1..{MAX_BYTES}",
              file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)

    with open(dest, "rb") as f:
        written = f.read()
    if written != data:
        print("error: written output differs from decoded image", file=sys.stderr)
        return 1

    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {dest} ({len(written)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
