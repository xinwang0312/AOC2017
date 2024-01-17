import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint



def init_matrix(lines: list[str], N:int=99) -> list[list[str]]:
    n = len(lines) + N * 2
    G = [['.' for i in range(n)] for j in range(n)]
    for j in range(len(lines)):
        for i in range(len(lines)):
            G[j + N][i + N] = lines[j][i]
    return G

def turn_left(face):
    return (face - 3) % 12


def turn_right(face):
    return (face + 3) % 12


def turn_back(face):
    return (face + 6) % 12


def move(face, y, x):
    mmap = {
        0: (-1, 0),
        3: (0, 1),
        6: (1, 0),
        9: (0, -1),
    }
    dy, dx = mmap[face]
    return y + dy, x + dx


def print_G(G):
    print('\n'.join(["".join(row) for row in G]))


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    N, n = (201, 10000) #if len(lines) > 10 else (3, 10000)
    G = init_matrix(lines, N=N)
    y, x = (len(G) // 2, len(G) // 2)
    print(f"size = {len(G)}, cen = {x}")
    face = 0

    num_inf = 0
    for i in range(n):
        if G[y][x] == '.':  # clean
            face = turn_left(face)
            G[y][x] = '#'
            num_inf += 1
        else:  # infected
            face = turn_right(face)
            G[y][x] = '.'
        y, x = move(face, y, x)
    print_G(G)
    print(f"{num_inf=}") 


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    
    N, n = (1001, 10000000) #if len(lines) > 10 else (3, 10000)
    G = init_matrix(lines, N=N)
    y, x = (len(G) // 2, len(G) // 2)
    print(f"size = {len(G)}, cen = {x}")
    face = 0

    num_inf = 0
    for i in range(n):
        if G[y][x] == '.':  # clean
            face = turn_left(face)
            G[y][x] = 'W'
        elif G[y][x] == 'W':  # weaken
            # face = face
            num_inf += 1
            G[y][x] = '#'
        elif G[y][x] == '#':  # infected
            face = turn_right(face)
            G[y][x] = 'F'
        elif G[y][x] == 'F':  # Flagged
            face = turn_back(face)
            G[y][x] = '.'
        else:
            raise ValueError(G[y][x])
        y, x = move(face, y, x)
    # print_G(G)
    print(f"{num_inf=}") 




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
