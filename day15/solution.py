import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint


def part1(input_file):
    fa, fb = 16807, 48271
    #a, b = 65, 8921
    a, b = 722, 354
    N = 40_000_000
    mask = 2147483647

    res_list = []
    for i in range(N):
        if i % 1000 == 0:
            print(f"========= {i} ============")
        a = (a * fa) % mask
        b = (b * fb) % mask
        #print(f"{a=}")
        #print(f"{b=}")
        if bin(a)[-16:] == bin(b)[-16:]:
            print(f'count +1 at {i}')
            res_list.append(i)
    print(f'res = {len(res_list)}')


def gen_numbers(x, fx, modx, n):
    res_list = []
    mask = 2147483647
    while len(res_list) < n:
        x = (x * fx) % mask
        if x % modx == 0:
            res_list.append(x)
    return res_list



def part2(input_file):
    fa, fb = 16807, 48271
    a, b = 65, 8921
    a, b = 721, 354
    N = 5_000_000

    a_list = gen_numbers(x=a, fx=fa, modx=4, n=N)
    print("a ready")
    b_list = gen_numbers(x=b, fx=fb, modx=8, n=N)
    print("b ready")
    res_list = [i for i, (a, b) in enumerate(zip(a_list, b_list)) if bin(a)[-16:] == bin(b)[-16:]]
    print(res_list)
    print(len(res_list))



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
