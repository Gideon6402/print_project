#!/usr/bin/env python3

import argparse
import logging


from traverse_and_concatenate import traverse_and_concatenate

def parse_arguments():
    parser = argparse.ArgumentParser(description="Concatenate Python project files into a single text file.")
    parser.add_argument('--root', required=True, help='Root directory of the Python project.')
    parser.add_argument('--output', required=True, help='Output text file path.')
    parser.add_argument('--ignore', default='.gitignore', help='Path to the ignore file.')
    return parser.parse_args()

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    args = parse_arguments()
    setup_logging()
    traverse_and_concatenate(args.root, args.output, args.ignore)

if __name__ == "__main__":
    main()
