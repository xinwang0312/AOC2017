import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint


def parse_input(lines):
    return lines[0].split(',')


def execute(move: str, programs: str) -> str:
    if move[0] == 's':
        return spin(programs, int(move[1:]))
    elif move[0] == 'x':
        return swap_ind(programs, tuple([int(x) for x in move[1:].split('/')]))
    elif move[0] == 'p':
        return swap(programs, tuple(move[1:].split('/')))
    else:
        raise ValueError(move)


def spin(programs: str, size: int) -> str:
    return programs[-size:] + programs[:-size]

def swap_ind(programs: str, indices: tuple[int, int]) -> str:
    prog_list = list(programs)
    prog_list[indices[0]], prog_list[indices[1]] = prog_list[indices[1]], prog_list[indices[0]]
    return ''.join(prog_list)


def swap(programs: str, letters: tuple[str, str]) -> str:
    return programs.replace(letters[0], '#').replace(letters[1], letters[0]).replace('#', letters[1])


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    moves = parse_input(lines)
    programs = 'abcdefghijklmnop'
    for move in moves:
        programs = execute(move, programs)

    print(programs)


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    moves = parse_input(lines)
    programs = 'abcdefghijklmnop'
    seen = []
    for i in range(100):
        for move in moves:
            programs = execute(move, programs)
        print(f"{i:4d}", programs)
        try:
            ind = seen.index(programs)
            #print(f"iter {i}: have been seen in iter {ind}")
            #break
        except ValueError:
            seen.append(programs)
    period = i
    print(f"{period=}")

    N = 1000000000
    print(seen[(N - 1) % period])



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
