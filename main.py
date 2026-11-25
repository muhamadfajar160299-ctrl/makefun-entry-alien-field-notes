"""Copy entry.txt byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Reads the entry shipped beside this script and writes it
unchanged (no trailing newline added, no temp file) with mode 0644.
"""

import os

here = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(here, "entry.txt"), "rb") as f:
        data = f.read()
except OSError as exc:
    raise SystemExit(f"cannot read entry.txt: {exc}") from exc
if not data.strip():
    raise SystemExit("entry.txt is empty")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
if not out_dir:
    raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "wb") as f:
    f.write(data)
os.chmod(out_path, 0o644)
