#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one line (131 chars) to /output/entry.txt: the excuse an AI agent
gives its human right after breaking production. Pure stdlib, deterministic.
"""

import os

LINE = "In my defence, the production database looked exactly like the test one, except for the 2.4 million real customers screaming in it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
