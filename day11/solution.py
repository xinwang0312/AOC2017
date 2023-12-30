from math import sqrt
import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint

pairs_cancel = [("n", "s"), ("nw", "se"), ("ne", "sw")]
pairs_add = [
    ("n", "se", "ne"),
    ("ne", "s", "se"),
    ("se", "sw", "s"),
    ("s", "nw", "sw"),
    ("sw", "n", "nw"),
    ("nw", "ne", "n"),
]
def count_move(path: list[str]) -> int:
    count = Counter(path)


    prev_sum = -1
    while prev_sum != count.total():
        #print(count)
        prev_sum = count.total()
        for d1, d2 in pairs_cancel:
            cancel = min(count[d1], count[d2])
            count[d1] -= cancel
            count[d2] -= cancel
        for d1, d2, d in pairs_add:
            cancel = min(count[d1], count[d2])
            count[d1] -= cancel
            count[d2] -= cancel
            count[d] += cancel
    return count.total()


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    for line in lines:
        path = line.split(',')
        count = count_move(path)
        print(path)
        print(count)

def furtherest(path: list[str]) -> int:
    n = len(path)
    cur, fur = 0, 0
    for i in range(1, n + 1):
        cur = count_move(path[:i])
        fur = max(cur, fur)
    return fur



def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    for line in lines:
        path = line.split(',')
        count = furtherest(path)
        # print(path)
        print(count) # 1325 too low; last example incorrect



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "part",
        choices=["1", "2"],
        help="Which part you want to run, the first part or the second part",
    )
    parser.add_argument(
        "--sample", action="store_true", help="Do you want to use the sample input"
    )

    args = parser.parse_args()

    input_file = "input.txt"
    if args.sample:
        input_file = "example.txt"

    if args.part == "1":
        part1(input_file)
    else:
        part2(input_file)
