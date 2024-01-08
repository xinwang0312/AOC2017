import argparse
import itertools
import os
import re
from collections import defaultdict, Counter, deque
from pprint import pprint


def parse_input(lines: list[str]) -> dict[int, tuple[int, int]]:
    return {i: tuple(int(x) for x in line.split('/', 2)) for i, line in enumerate(lines)}


def get_port_dict(components: dict[int, tuple[int, int]]) -> dict:
    port_dict = {}
    for ind, ports in components.items():
        for port in ports:
            if port in port_dict.keys():
                port_dict[port].append(ind)
            else:
                port_dict[port] = [ind]
    return port_dict


def get_other_port(port: int, ports: tuple[int, int]):
    assert port in ports
    other_port = set(ports) - {port}
    if len(other_port) > 0:
        return other_port.pop()
    else:
        return port  # two same port


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    components = parse_input(lines)
    port_dict = get_port_dict(components)
    print(port_dict)

    to_visit = deque(
        [(sum(components[c]), c, 0, [c]) for c in port_dict[0]]
    )
    strongest = (0, -1, 0, [])
    
    while len(to_visit) > 0:
        # print(f"len = {len(to_visit)}")
        score, cur_id, cur_port, used = to_visit.pop()
        other_port = get_other_port(cur_port, components[cur_id])
        other_comp = set(port_dict[other_port]) - set(used)
        for comp in other_comp:
            to_visit.append(
                (score + sum(components[comp]), comp, other_port, used + [comp])
            )
        if score > strongest[0]:
            strongest = (score, cur_id, cur_port, used)

    print(strongest)
    for i in strongest[3]:
        print(components[i])


    



def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    components = parse_input(lines)
    port_dict = get_port_dict(components)

    to_visit = deque(
        [(sum(components[c]), c, 0, [c]) for c in port_dict[0]]
    )
    longest = (0, -1, 0, [])
    
    while len(to_visit) > 0:
        # print(f"len = {len(to_visit)}")
        score, cur_id, cur_port, used = to_visit.pop()
        other_port = get_other_port(cur_port, components[cur_id])
        other_comp = set(port_dict[other_port]) - set(used)
        for comp in other_comp:
            to_visit.append(
                (score + sum(components[comp]), comp, other_port, used + [comp])
            )
        if len(used) > len(longest[3]):
            longest = (score, cur_id, cur_port, used)
        elif len(used) == len(longest[3]):
            if score > longest[0]:
                longest = (score, cur_id, cur_port, used)

    print(longest)
    print(len(longest[3]))



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
