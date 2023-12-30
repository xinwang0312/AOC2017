import networkx as nx
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


def knot_hash(string) -> str:
    N = 256
    lengths = [ord(s) for s in string] + [17, 31, 73, 47, 23]
    numbers = list(range(N))
    cur_pos = 0
    skip_size = 0

    for j in range(64):
        for i, length in enumerate(lengths):
            # print(f'---- {length=}, {skip_size=}, cur = {numbers[cur_pos]} ----')
            numbers, cur_pos, skip_size = execute(numbers, cur_pos, skip_size, length)

    sparse_hash = numbers
    dense_hash = []
    for i in range(16):
        xor = reduce(lambda x, y: x ^ y, sparse_hash[i * 16: (i + 1) * 16])
        dense_hash.append(f"{xor:08b}")
        # dense_hash.append(xor)

    return "".join(dense_hash)



def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    string = lines[0]
    res = 0
    pretty = []
    for i in range(128):
        h_str = string + f"-{i}"
        h = knot_hash(h_str)
        pretty.append(h.replace('1', '#').replace('0', '.'))
        res += h.count('1')
    print(f"{res=}")

    with open(input_file.replace('.txt', '_mat.txt'), 'w') as f:
        f.write('\n'.join(pretty))
    return pretty



def part2(input_file):
    with open(input_file.replace('.txt', '_mat.txt')) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    G = nx.Graph()
    for j, row in enumerate(lines):
        for i, s in enumerate(row):
            if s == "#":
                G.add_node((j, i))

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for y, x in G.nodes:
        for dy, dx in dirs:
            y1, x1 = y + dy, x + dx
            if (y1, x1) in G.nodes:
                G.add_edge((y, x), (y1, x1))

    res = [c for c in nx.connected_components(G)]
    print(len(res))



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
