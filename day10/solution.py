from functools import reduce
import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint


def execute(numbers: list[int], cur_pos: int, skip_size: int, length: int) -> list[int]:
    numbers = reverse(numbers, cur_pos, length)
    cur_pos = (cur_pos + skip_size + length) % len(numbers)
    skip_size += 1
    return numbers, cur_pos, skip_size


def reverse(numbers: list[int], cur_pos: int, length: int) -> list[int]:
    n = len(numbers)
    dup_num = numbers + numbers
    rev_num = dup_num[cur_pos: cur_pos + length].copy()
    rev_num.reverse()
    other_num = dup_num[cur_pos + length: cur_pos + n]
    new_num = rev_num + other_num
    split = n - cur_pos
    ret_num = new_num[split:] + new_num[:split]
    assert len(ret_num) == len(numbers)
    return ret_num



def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    N = 256 if len(lines[0]) > 18 else 5
    numbers = list(range(N))
    cur_pos = 0
    skip_size = 0
    lengths = [int(x) for x in lines[0].split(',')]

    for i, length in enumerate(lengths):
        print(f'---- {length=}, {skip_size=}, cur = {numbers[cur_pos]} ----')
        numbers, cur_pos, skip_size = execute(numbers, cur_pos, skip_size, length)
        print(numbers)
    print(f"res = {numbers[0] * numbers[1]}")




def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    N = 256 
    lengths = [ord(s) for s in lines[0]] + [17, 31, 73, 47, 23]
    numbers = list(range(N))
    cur_pos = 0
    skip_size = 0

    for j in range(64):
        print(f"========== round {j} =============")
        for i, length in enumerate(lengths):
            # print(f'---- {length=}, {skip_size=}, cur = {numbers[cur_pos]} ----')
            numbers, cur_pos, skip_size = execute(numbers, cur_pos, skip_size, length)
 
    sparse_hash = numbers
    dense_hash = []
    for i in range(16):
        xor = reduce(lambda x, y: x ^ y, sparse_hash[i * 16: (i + 1) * 16])
        dense_hash.append(f"{xor:02x}")

    print(dense_hash)
    print("".join(dense_hash))

    return 0



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
