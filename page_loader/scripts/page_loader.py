#!/usr/bin/env python3

from page_loader import cli


def main():
    args = cli.parser.parse_args()
    cli.run(args)


if __name__ == '__main__':
    main()
