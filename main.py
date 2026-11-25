#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a freshly liquidated crypto trader
to /output/entry.txt, with no trailing newline.
"""

LINE = (
    "You were liquidated, yet this cookie is unbroken. "
    "Take the omen kindly: something in you, too, refuses to crumble."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
