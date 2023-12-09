import argparse
import itertools
import os
import re
from collections import defaultdict, Counter


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    digits = [int(x) for x  in lines[0]]
    digits.append(digits[0])

    eq = [x0 if x0 == x1 else 0 for x0, x1 in zip(digits[:-1], digits[1:])]
    print(sum(eq))


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    digits = [int(x) for x  in lines[0]]
    n = len(digits)

    digits = digits[n//2: ] + digits

    eq = [x0 if x0 == x1 else 0 for x0, x1 in zip(digits[n//2:], digits[:-n//2])]
    print(sum(eq))





if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("part", choices=["1", "2"], help="Which part you want to run, the first part or the second part")
    parser.add_argument("--sample", action="store_true", help="Do you want to use the sample input")

    args = parser.parse_args()

    input_file = "input.txt"
    if args.sample:
        input_file = "example.txt"

    if args.part == "1":
        part1(input_file)
    else:
        part2(input_file)
