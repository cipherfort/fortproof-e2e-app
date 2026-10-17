"""Reads a YAML settings file and prints it."""

import sys

import yaml


def main() -> None:
    with open(sys.argv[1], encoding="utf-8") as f:
        print(yaml.safe_load(f))


if __name__ == "__main__":
    main()
