import argparse
import itertools
import os
import re
from collections import defaultdict, Counter


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    res = 0
    for line in lines:
        words = line.split(' ')
        if len(set(words)) == len(words):
            res += 1
    print(res)



def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    res = 0
    for line in lines:
        words = line.split(' ')
        for w1, w2 in itertools.combinations(words, 2):
            if Counter(w1) == Counter(w2):
                res += 1
                break
    print(len(lines) - res)



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
