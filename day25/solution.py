import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint



def part1_sample():
    write = {
        'A': {0: 1, 1: 0},
        'B': {0: 1, 1: 1}
    }
    move = {
        'A': {0: 1, 1: -1},
        'B': {0: -1, 1: 1}
    }
    nxt = {
        'A': {0: 'B', 1: 'B'},
        'B': {0: 'A', 1: 'A'},
    }


    N = 7
    tape = [0] * N
    cur = N // 2
    state = 'A'
    
    n = 7
    print(tape, cur)
    for i in range(n):
        cur_value = tape[cur] 
        tape[cur] = write[state][cur_value]
        cur += move[state][cur_value]
        state = nxt[state][cur_value]
        print(tape, cur, state)

def part1():
    write = {
        'A': {0: 1, 1: 0},
        'B': {0: 1, 1: 0},
        'C': {0: 1, 1: 1},
        'D': {0: 0, 1: 1},
        'E': {0: 1, 1: 0},
        'F': {0: 0, 1: 0},
    }
    move = {
        'A': {0: 1, 1: -1},
        'B': {0: 1, 1: 1},
        'C': {0: -1, 1: -1},
        'D': {0: -1, 1: 1},
        'E': {0: -1, 1: 1},
        'F': {0: 1, 1: 1},
    }
    nxt = {
        'A': {0: 'B', 1: 'D'},
        'B': {0: 'C', 1: 'F'},
        'C': {0: 'C', 1: 'A'},
        'D': {0: 'E', 1: 'A'},
        'E': {0: 'A', 1: 'B'},
        'F': {0: 'C', 1: 'E'},
    }

    N = 50001
    tape = [0] * N
    cur = N // 2
    state = 'A'
    
    n = 12317297
    for i in range(n):
        cur_value = tape[cur] 
        tape[cur] = write[state][cur_value]
        cur += move[state][cur_value]
        state = nxt[state][cur_value]
        if i % 1_000_000 == 0:
            print(i, sum(tape))
    print(sum(tape))



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
        part1()
    else:
        part2(input_file)
