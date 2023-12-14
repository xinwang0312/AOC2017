import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from functools import cache


def parse_input(lines):
    pattern = r'([a-z]+) \((\d+)\)(?: -> ((?:[a-z]+, )*[a-z]+))?'
    parent_dict = {}
    weight_dict = {}
    for line in lines:
        match = re.search(pattern, line)
        if match:
            weight_dict[match.group(1)] = int(match.group(2))
            if match.group(3):
                parent_dict[match.group(1)] = [s.strip() for s in match.group(3).split(',')]
        else:
            raise ValueError(line)
    return parent_dict, weight_dict


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    parent_dict, weight_dict = parse_input(lines)
    print(parent_dict)
    all_children = set()
    for v in parent_dict.values():
        all_children = all_children | set(v)
    res = set(parent_dict.keys()) - all_children
    print(res)
    return res


def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    parent_dict, weight_dict = parse_input(lines)
    # print(parent_dict)
    # print(weight_dict)
    #bottom = part1(input_file)

    @cache
    def cal_disc_weight(name):
        weight = weight_dict[name]
        if name in parent_dict.keys():
            for child in parent_dict[name]:
                weight += cal_disc_weight(child)
        return weight
    
    ub_parents, ub_children, possible_results = [], [], []
    for ii, (parent, children) in enumerate(parent_dict.items()):
        children_weight = [cal_disc_weight(child) for child in children]
        if len(set(children_weight)) > 1:
            counter = Counter(children_weight).most_common(2)
            unbalance_child = children[children_weight.index(counter[1][0])]
            orig_weight = weight_dict[unbalance_child]
            delta = counter[0][0] - counter[1][0]
            ub_parents.append(parent)
            ub_children.append(children)
            possible_results.append(orig_weight + delta)
            print(f"------------{ii}--------------")
            print(parent, children)
            print(orig_weight + delta)
            # return 0

    # the unbalance will propergate upwards, we need to find the lowest one
    for p, c, r in zip(ub_parents, ub_children, possible_results):
        if len(set(c) & set(ub_parents)) == 0:
            print(f"res = {r}")
            return None



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
