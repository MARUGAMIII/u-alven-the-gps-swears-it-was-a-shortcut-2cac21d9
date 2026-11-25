#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut -- make.fun entry.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Craft notes (v2, revised): the GPS blames the map, stays smug and
defensive ("unlike you I trust my sources"), and lands on a fresh,
specific detail -- a lake the map called a shortcut, with ducks
laughing at driver and GPS alike. Revision: dropped the redundant
"I believed it, because" so the line reads in one breath and the
punchline lands sooner; the joke, the blame and the ducks are
unchanged. One line, plain ASCII, no em dash.

Python standard library only.
"""

import os

ENTRY = (
    "The map labeled the lake a shortcut, and unlike you "
    "I trust my sources, so now the ducks are laughing at us both."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
