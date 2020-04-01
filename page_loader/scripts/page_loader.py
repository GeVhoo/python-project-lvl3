#!/usr/bin/env python3

import sys

from page_loader import cli
from page_loader import engine

from page_loader.logger import set_logger
from page_loader.storage import url_normalization


def main():
    args = cli.parser.parse_args()
    set_logger(args.level)
    try:
        engine.run(url_normalization(args.url), args.output)
    except Exception:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
