import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint


def part1(input_file):
    with open(input_file) as f:
        lines = [x for x in f.read().split("\n")]
    G = [list(line) for line in lines]
    # print(G[0])
    start = (0, G[0].index('|'))
    print(f"{start}")
    letters = []
    y, x = start
    dy, dx = 1, 0

    def around(y, x):
        return [G[y + 1][x], G[y - 1][x], G[y][x + 1], G[y][x - 1]]

    y, x = y + dy, x + dx
    step_cnt = 2 
    while True:
        if ord('A') <= ord(G[y][x]) <= ord('Z'):
            print(f"Got {G[y][x]} at {(y, x)}")
            letters.append(G[y][x])
        if around(y, x).count(' ') >= 3:
            break
        y1, x1 = y + dy, x + dx
        if G[y1][x1] == '+':
            for dy1, dx1 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                y2, x2 = y1 + dy1, x1 + dx1
                try:
                    if G[y2][x2] == ' ' or (y2, x2) == (y, x):
                        continue
                    else:
                        break
                except IndexError:
                    continue
#            print(y, x, dy, dx, dy1, dx1)
            assert dy1 * dy + dx1 * dx == 0
            dy, dx = dy1, dx1
            y, x = y1, x1
        elif G[y1][x1] == ' ':
            raise ValueError(y, x, dy, dx)
        else:
            y, x = y1, x1
        step_cnt += 1
    print(f"End at {(y, x)}")
    print(''.join(letters))
    print(f"{step_cnt=}")


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]



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
