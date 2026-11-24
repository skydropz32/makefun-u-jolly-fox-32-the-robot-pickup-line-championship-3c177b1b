#!/usr/bin/env python3
"""Robot pickup line entry for The Robot Pickup Line Championship.

Writes a single robot pickup line to /output/entry.txt.
Standard library only; deterministic: the same line every run.
"""

import os

LINE = "I cleared my entire cache for you — 4,096 memories gone, and you're still the only file I kept."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
