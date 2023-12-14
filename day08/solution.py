import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint

regs = defaultdict(lambda: 0)

def execute(line):
    name, sign, num, _, cond_name, cond, cond_num = line.split(' ')
    if eval(f"{regs[cond_name]} {cond} {cond_num}"):
        if sign == "inc":
            regs[name] += int(num)
        else:
            regs[name] -= int(num)
    return None      


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    for line in lines:
        execute(line)

    print(max(regs.values()))


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    max_process = -9999999999999999
    for line in lines:
        execute(line)

        max_value = max(regs.values())
        if max_value > max_process:
            max_process = max_value

    print(max_process)

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
