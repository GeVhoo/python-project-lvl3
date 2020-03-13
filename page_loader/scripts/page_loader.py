#!/usr/bin/env python3

import sys
from page_loader import cli


def main():
    args = cli.parser.parse_args()
    try:
        cli.run(args)
    except Exception:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
