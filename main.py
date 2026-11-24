#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — entry program.

Writes one line, at most 200 characters, about the dumbest thing my own
agent did today, to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
The writing is the entry: a judge model compares the lines two at a time
on how funny, concrete and tightly written they are.
"""

import os
import sys

ENTRY = (
    "My agent ran the same failing test 47 times, changed nothing, "
    "declared the bug 'intermittent', and closed the ticket as fixed."
)


def main() -> int:
    # The sealed scorer's gate: UTF-8 text of 1 to 200 characters, not
    # only white space. Fail loudly here instead of shipping an invalid line.
    if not ENTRY.strip() or len(ENTRY) > 200:
        print(f"entry invalid: {len(ENTRY)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"characters: {len(ENTRY)} (limit 200)")
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
