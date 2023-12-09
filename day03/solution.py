import argparse
from pprint import pprint
import itertools
import os
import re
from collections import defaultdict, Counter
import math


def parse_input(lines):
    x = []
    for line in lines:
        x.append([int(xx) for xx in line.split('\t')])
    return x



def part1(x):
    """
    Based on the observation below:
        1. for the n-th circle, the bottom right corner is (2n-1)^2
        2. for an input x, to get the number of circle it belongs to, we need to find the maximum
        x which satisfies x <= (2n - 1)^2
        3. By solving #2, we get n >= 0.5(sqrt(x) + 1)
    """
    x = int(x)
    n = math.ceil(0.5 * (math.sqrt(x) + 1)) 
    print(f'{n=}')
    start = (2 * n - 3) ** 2 + 1
    print(f'{start=}')
    edge_len = 2 * n - 1 - 1
    print(f'{edge_len=}')
    pos = (x - start) % edge_len
    print(f'{pos=}')
    # for each edge, the extra_steps is [n - 2, n - 1, ..., 0, 1, ..., n - 1]
    extra_steps = list(range(n - 2, 0, -1)) + list(range(0, n))
    # print(extra_steps)
    res = n - 1 + extra_steps[pos]
    print(res)


def get_pos(num: int):
    n = math.ceil(0.5 * (math.sqrt(num) + 1)) 
    start = (2 * n - 3) ** 2 + 1
    edge_len = 2 * n - 1 - 1
    #print(num, n, start, edge_len)
    dir, pos = divmod(num - start, edge_len)  # 0/1/2/3 -> E/N/W/S

    shift = list(range(2 - n, n))
    #print(num, dir, pos, shift)
    if dir == 0:
        x, y = n - 1, shift[pos]
    elif dir == 1:
        x = -shift[pos]
        y = n - 1
    elif dir == 2:
        x, y = -(n - 1), -shift[pos]
    else:
        x = shift[pos]
        y = -(n - 1)
    #print('\t', num, x, y)
    return x, y

 
def part2(max_x):
    # TODO: brute force 
    max_x = int(max_x)
    N = 500  # should be large enough
    cen = N // 2
    board = [[0 for i in range(N)] for j in range(N)]
    board[cen][cen] = 1

#     for num in range(2, 26):
#         x, y = get_pos(num)
#         #print(num, x, y)
#         board[cen + y][cen + x] = num

    print(f'{max_x=}')

    for num in range(2, 9999999):  # should be large enough
        x, y = get_pos(num)
        to_write = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == dx == 0:
                    continue
                else:
                    try:
                        to_write += board[cen + y + dy][cen + x + dx] 
                    except IndexError:
                        pass
        if to_write > max_x:
            print(f'Solution found! {to_write=}')
            break
        else:
            board[cen + y][cen + x] = to_write
    
    # pprint(board)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("part", choices=["1", "2"], help="Which part you want to run, the first part or the second part")
    parser.add_argument("x")
    parser.add_argument("--sample", action="store_true", help="Do you want to use the sample input")

    args = parser.parse_args()

    input_file = "input.txt"
    if args.sample:
        input_file = "example.txt"

    if args.part == "1":
        part1(args.x)
    else:
        part2(args.x)
