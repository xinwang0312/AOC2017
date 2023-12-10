import argparse
import itertools
import os
import re
from collections import defaultdict, Counter


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    offsets = [int(x) for x in lines]
    cnt = 1
    cur = 0
    while True:
        nxt = cur + offsets[cur]
        if nxt >= len(offsets):
            print(offsets)
            print(f'{cnt=}')
            return cnt
        else:
            offsets[cur] += 1
            cnt += 1
        # print('---------------------------')
        # print(cnt, cur, nxt)
        # print(offsets)
        cur = nxt





def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    offsets = [int(x) for x in lines]
    cnt = 1
    cur = 0
    while True:
        nxt = cur + offsets[cur]
        if nxt >= len(offsets):
            print(offsets)
            print(f'{cnt=}')
            return cnt
        else:
            if offsets[cur] >= 3:
                offsets[cur] -= 1
            else:
                offsets[cur] += 1
            cnt += 1
        # print('---------------------------')
        # print(cnt, cur, nxt)
        # print(offsets)
        cur = nxt




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
