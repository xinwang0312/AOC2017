import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint



def insert(array: list[int], num: int, cur: int, step: int) -> tuple[list[int], int]:
    ind = (cur + step) % len(array) + 1
    array.insert(ind, num)
    return array, ind

def part1(input_file):
    step = 312
    array = [0]
    cur = 0
    for i in range(1, 2017 + 1):
        array, cur = insert(array, i, cur, step)
        # print(array, cur)
    ind = array.index(2017)
    print(array[ind + 1])


def part2_bf(input_file):
    step = 312
    array = [0]
    cur = 0
    for i in range(1, 50_0 + 1):
        array, cur = insert(array, i, cur, step)
        if cur == 1:
            print(i, array)
        if i % 1_000_000 == 0:
            print(f"{i / 1_000_000} / 50")


def part2(input_file):
    s = 312
    n, l = 1, 2
    N = 50_000_000

    for i in range(2, N + 1):
        n = (n + s) % i + 1
        if n == 1:
            print(i)





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
