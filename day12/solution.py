import argparse
import itertools
import os
import re
from collections import defaultdict, Counter, deque
from pprint import pprint


def parse_input(lines):
    links = {}
    for line in lines:
        start, end = line.split('<->')
        links[int(start.strip())] = [int(x.strip()) for x in end.split(',')]
    return links


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    links = parse_input(lines)
    connected = {0}
    queue = deque([0])

    while len(queue) > 0:
        u = queue.popleft()
        for v in links[u]:
            if v not in connected:
                connected.add(v)
                queue.append(v)

    print(f"res = {len(connected)}")


def get_groups(u, links):
    connected = {u}
    queue = deque([u])

    while len(queue) > 0:
        u = queue.popleft()
        for v in links[u]:
            if v not in connected:
                connected.add(v)
                queue.append(v)
    return connected






def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    links = parse_input(lines)
    remain_nums = set(links.keys())

    groups = []
    while len(remain_nums) > 0:
        u = remain_nums.pop()
        connected = get_groups(u, links)
        print(f"{u=}, group size = {len(connected)}")
        groups.append(u)
        remain_nums -= connected
    print(groups)
    print(len(groups))



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
