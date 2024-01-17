import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint


def transpose(G):
    return list(map(list, zip(*G)))

def rotate(G):
    return list(map(list, zip(*G[::-1])))


def variant(G):
    v = [G, transpose(G)]
    for i in range(3):
        G = rotate(G)
        v.append(G)
        v.append(transpose(G))
    return ['/'.join([''.join(row) for row in vi]) for vi in v]


def print_matrix(G):
    print('\n'.join([''.join(row) for row in G]))


def reconstruct(s: str) -> list[list[str]]:
    return [list(line) for line in s.split('/')]


def apply(M, rules_2, rules_3):
    n = len(M)
    if n % 2 == 0:
        step = 2
        rules = rules_2
    elif n % 3 == 0:
        step = 3
        rules = rules_3
    else:
        raise ValueError(M, n)
    print(f'n = {n}, num of rules = {len(rules)}')
    # print(rules)
    
    transformed = []
    for j in range(0, n, step):
        transformed_row = []
        for i in range(0, n, step):
            G = [row[i: i + step] for row in M[j: j + step]]
            # print(G)
            variants = variant(G)
            key = list(set(variants) & set(rules.keys()))
            if len(key) == 1:
                transformed_row.append(reconstruct(rules[key[0]]))
            else:
                print(f"{variants=}")
                print("rules=", rules.keys())
                print('==============')
                raise ValueError(key) 
        for rows in zip(*transformed_row):
            # print(rows)
            if len(rows) > 1:
                transformed.append(sum(rows, []))
            else:
                transformed.append(rows[0])
    return transformed



def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    rules = {x[0]: x[1] for x in [line.split(' => ') for line in lines]}
    rules_2 = {k: v for k, v in rules.items() if len(k) == 5}
    rules_3 = {k: v for k, v in rules.items() if len(k) == 11}
    N = 5

    matrix = reconstruct( '.#./..#/###')

    print(f"------- start ------------")
    for i in range(N):
        print(f'------ iter {i + 1} -----')
        matrix = apply(matrix, rules_2, rules_3)
        # print(matrix)

    print(Counter(sum(matrix, []))["#"])




def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    rules = {x[0]: x[1] for x in [line.split(' => ') for line in lines]}
    rules_2 = {k: v for k, v in rules.items() if len(k) == 5}
    rules_3 = {k: v for k, v in rules.items() if len(k) == 11}
    N = 18

    matrix = reconstruct( '.#./..#/###')

    print(f"------- start ------------")
    for i in range(N):
        print(f'------ iter {i + 1} -----')
        matrix = apply(matrix, rules_2, rules_3)
        # print(matrix)

    print(Counter(sum(matrix, []))["#"])




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
