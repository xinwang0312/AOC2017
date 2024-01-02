import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint
from math import sqrt


def distance(s0, v, a, T):
    return v * T + a * T ** 2 / 2 + s0


def distance_3d(p, v, a, T):
    return sum([abs(distance(pi, vi, ai, T)) for pi, vi, ai in zip(p, v, a)])


def parse_line(line):
    pattern = r'[-+]?\d+'
    numbers = re.findall(pattern, line)
    numbers = [int(x) for x in numbers]
    p, v, a = numbers[:3], numbers[3:6], numbers[6:]
    if not len(p) == len(v) == len(a) == 3:
        raise ValueError(line, p, v, a)
    return p, v, a

def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    distances = []
    T = 999999
    for line in lines:
        p, v, a = parse_line(line)
        dis = distance_3d(p, v, a, T)
        distances.append(dis)
    
    ind, dis = min(enumerate(distances), key=lambda x: x[0])
    print(ind, dis)


def sol_quad_eq(a, b, c) -> set[float] | None:
    n = 10
    res = set()
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta >= 0:
            r1 = (-b + sqrt(delta)) / (2 * a)
            r2 = (-b - sqrt(delta)) / (2 * a)
            if int(r1) == r1:
                res.add(r1)
            if int(r2) == r2:
                res.add(r2)
    else:
        if b != 0:
            r1 = -c / b
            if int(r1) == r1:
                res.add(r1)
        else:
            if c == 0:
                return None

    return res

def collide(p1, v1, a1, p2, v2, a2):
    t = []
    for p1i, v1i, a1i, p2i, v2i, a2i in zip(p1, v1, a1, p2, v2, a2):
        sol = sol_quad_eq((a1i - a2i), (a1i - a2i) + 2 * (v1i - v2i), 2 * (p1i - p2i))
        t.append(sol)

    t = set.intersection(*[ti for ti in t if ti is not None])
    t_c = [ti for ti in t if ti > 0]
    return t_c



def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    n = len(lines)
    destroy = {i: {} for i in range(n)}
    collide_time = {}
    for i, j in itertools.combinations(range(n), 2):
        p1, v1, a1 = parse_line(lines[i])
        p2, v2, a2 = parse_line(lines[j])
        try:
            t_c = collide(p1, v1, a1, p2, v2, a2)
        except ValueError as e:
            print(i, j, p1, v1, a1, p2, v2, a2)
            raise e
        if len(t_c) > 0:
            print(f"{i} will collide with {j} at {t_c}")
            destroy[i][j] = t_c[0]
            destroy[j][i] = t_c[0]
            if t_c[0] in collide_time.keys():
                collide_time[t_c[0]].append((i, j))
            else:
                collide_time[t_c[0]] = [(i, j)]
    ticks = sorted(collide_time.keys())
    remain = set(range(n))

    # print(collide_time)
    for t in ticks:
        to_remove = set()
        for i, j in collide_time[t]:
            if j in remain and i in remain:
                to_remove.add(i)
                to_remove.add(j)
        remain = remain - to_remove

    print(f"{len(remain)}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("part", choices=["1", "2"], help="Which part you want to run, the first part or the second part")
    parser.add_argument("--sample", action="store_true", help="Do you want to use the sample input")

    args = parser.parse_args()

    input_file = "input.txt"
    if args.sample:
        input_file = "example2.txt"

    if args.part == "1":
        part1(input_file)
    else:
        part2(input_file)
