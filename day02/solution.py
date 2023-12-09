import argparse
import itertools
import os
import re
from collections import defaultdict, Counter


def parse_input(lines):
    x = []
    for line in lines:
        x.append([int(xx) for xx in line.split('\t')])
    return x



def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    numbers = parse_input(lines=lines)
    print(numbers)
    checksum = [max(array) - min(array) for array in numbers]
    print(sum(checksum))

def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    numbers = parse_input(lines)
    res = 0
    for array in numbers:
        for x1, x2 in itertools.permutations(array, 2):
            if x1 % x2 == 0:
                res += x1 / x2
                break
    print(res)
    




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
