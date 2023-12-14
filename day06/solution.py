import argparse
import itertools
import os
import re
from collections import defaultdict, Counter



def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    blocks = [int(x) for x in lines[0].split('\t') if x is not ""]
    n = len(blocks)
    cnt = 0
    cur = blocks
    seen = [tuple(blocks)]
    while True:
        print(f"{cnt}: {cur}")
        max_x = max(cur)
        max_ind = cur.index(max_x)
        if max_x >= n - 1:
            give, keep = divmod(max_x, n - 1)
            nxt = [x + give if i != max_ind else keep for i, x in enumerate(cur)]
        else:
            nxt = cur
            for i in range(max_ind + 1, max_ind + 1 + max_x):
                nxt[i % n] += 1
            nxt[max_ind] = 0
        cnt += 1
        if tuple(nxt) in seen:
            print(cnt)
            break
        else:
            cur = nxt
            seen.append(tuple(nxt))
        






def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    blocks = [int(x) for x in lines[0].split('\t') if x is not ""]
    n = len(blocks)
    cnt = 0
    cur = blocks
    seen = [tuple(blocks)]
    while True:
        # print(f"{cnt}: {cur}")
        max_x = max(cur)
        max_ind = cur.index(max_x)
        if max_x >= n - 1:
            give, keep = divmod(max_x, n - 1)
            nxt = [x + give if i != max_ind else keep for i, x in enumerate(cur)]
        else:
            nxt = cur
            for i in range(max_ind + 1, max_ind + 1 + max_x):
                nxt[i % n] += 1
            nxt[max_ind] = 0
        cnt += 1
        if tuple(nxt) in seen:
            print(cnt)
            prev_seen = seen.index(tuple(nxt))
            print(cnt - prev_seen)
            break
        else:
            cur = nxt
            seen.append(tuple(nxt))


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
