import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint


def parse_input(lines):
    firewall = {}
    for line in lines:
        a, b = line.split(': ')
        firewall[int(a)] = int(b)
    print(firewall)
    return firewall

def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    firewall = parse_input(lines)
    severity = 0
    for layer, thickness in firewall.items():
        if (layer) % (2 * (thickness - 1)) == 0:
            print(f"caught at {layer}")
            severity += layer * thickness
        
    print(f"{severity=}")


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    firewall = parse_input(lines)
    MAX_NUM = 100_000_00
    remain_nums = set(range(MAX_NUM))
    for layer, thickness in firewall.items():
        period = 2 * (thickness - 1)
        remove_nums = set(range(period - layer, MAX_NUM, period)) 
        # print(layer, remove_nums)
        remain_nums -= remove_nums
    print(min(remain_nums))


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
