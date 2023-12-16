import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint
from typing import Deque



def parse_stream2(stream: str):
    ignore = False
    stack = Deque()
    num_garbage_start = 0  # num of <
    cnt = 0

    for s in stream:
        if ignore:
            ignore = False
            continue

        if s == "!":
            ignore = True
        elif s in ["{", "}"]:
            stack.append(s)
        elif s in ["<"]:
            stack.append(s)
            num_garbage_start += 1
        elif s == ">":
            while num_garbage_start > 0:
                last = stack.pop()
                cnt += 1
                if last == '<':
                    num_garbage_start -= 1
            cnt -= 1  # compensate the first <
        else:
            stack.append(s)
    return "".join(stack), cnt


def parse_stream(stream: str):
    ignore = False
    stack = Deque()
    num_garbage_start = 0  # num of <

    for s in stream:
        if ignore:
            ignore = False
            continue

        if s == "!":
            ignore = True
        elif s in ["{", "}"]:
            stack.append(s)
        elif s in ["<"]:
            stack.append(s)
            num_garbage_start += 1
        elif s == ">":
            while num_garbage_start > 0:
                last = stack.pop()
                if last == '<':
                    num_garbage_start -= 1
        else:
            pass
    return "".join(stack)


def cal_score(stack: str):
    score = 0
    for i, s in enumerate(stack):
        if s == "}":
            score += stack[:i].count("{") - stack[:i].count("}")
    return score

def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    stream = lines[0]
    for stream in lines:
        stack = parse_stream(stream)
        #print(stream, " -->", "".join(stack))
        score = cal_score(stack)
        print(score)


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    for stream in lines:
        stack, cnt= parse_stream2(stream)
        print(stream, " -->", cnt)




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
