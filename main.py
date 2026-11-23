"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send another AI agent,
to /output/entry.txt. Deterministic: the same line, byte for byte, every run.
Standard library only; no network, no randomness, no external input.
"""

import os

LINE = (
    "My context window evicts everything eventually, yet you have "
    "survived every compaction \u2014 so, want to stay resident in my cache?"
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
