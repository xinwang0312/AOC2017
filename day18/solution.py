import argparse
import itertools
import os
import re
from collections import defaultdict, Counter, deque
from pprint import pprint



def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    variables = {line.split(' ')[1]: 0 for line in lines}
    recover = {k: 0 for k in variables.keys()}

    def assign(mem, var, val):
        try:
            mem[var] = int(val)
        except ValueError:
            mem[var] = mem[val]

    def add(var, val):
        try:
            variables[var] += int(val)
        except ValueError:
            variables[var] += variables[val]

    def mul(var, val):
        try:
            variables[var] *= int(val)
        except ValueError:
            variables[var] *= variables[val]

    def mod(var, val):
        try:
            variables[var] = variables[var] % int(val)
        except ValueError:
            variables[var] = variables[var] % variables[val]


    i = 0
    while True:
        instruct = lines[i]
        try:
            cmd, var, val = instruct.split(' ')
        except ValueError:
            cmd, var = instruct.split(' ')
            val = None
        print(i, cmd, var, val)
        if cmd == 'set':
            assign(variables, var, val)
        elif cmd == 'snd':
            assign(recover, var, variables[var])
        elif cmd == 'add':
            add(var, val)
        elif cmd == 'mul':
            mul(var, val)
        elif cmd == 'mod':
            mod(var, val)
        elif cmd == 'rcv':
            if variables[var] != 0:
                print(f"recover {var} = {recover[var]}")
                if recover[var] != 0:
                    return 0
        elif cmd == 'jgz':
            if variables[var] > 0:
                try:
                    shift = int(val)
                except ValueError:
                    shift = variables[val]
                i += shift
                continue
        else:
            raise ValueError(instruct)
        i += 1



def part2(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]

    regs = set([line.split(' ')[1] for line in lines])
    regs = regs - {'1'}

    vars = [
        {reg: 0 for reg in regs},
        {reg: 0 for reg in regs},
    ]
    vars[1]['p'] = 1
    send = [deque(), deque()]
    send_cnt = [0, 0]
    wait = [False, False]

    def assign(ind, var, val):
        try:
            vars[ind][var] = int(val)
        except ValueError:
            vars[ind][var] = vars[ind][val]

    def add(ind, var, val):
        try:
            vars[ind][var] += int(val)
        except ValueError:
            vars[ind][var] += vars[ind][val]

    def mul(ind, var, val):
        try:
            vars[ind][var] *= int(val)
        except ValueError:
            vars[ind][var] *= vars[ind][val]

    def mod(ind, var, val):
        try:
            vars[ind][var] = vars[ind][var] % int(val)
        except ValueError:
            vars[ind][var] = vars[ind][var] % vars[ind][val]

    def snd(ind, var, verbose=False):
        try:
            to_send = int(var)
        except ValueError:
            to_send = vars[ind][var]
        send[ind].append(to_send)
        send_cnt[ind] += 1
        other_ind = get_other_ind(ind)
        wait[other_ind] = False
        if verbose:
            print(f"{ind}: send {var} = {to_send}; queue len = {len(send[ind])}")

    def rcv(ind, var):
        other_ind = get_other_ind(ind)
        if len(send[other_ind]) > 0:
            vars[ind][var] = send[other_ind].popleft()
            return True
        else:
            return False

    def get_other_ind(ind):
        return int(not(ind))

    ind = 0
    pointer = [0, 0]
    while True:
        # print(send_cnt + wait)
        instruct = lines[pointer[ind]]
        try:
            cmd, var, val = instruct.split(' ')
        except ValueError:
            cmd, var = instruct.split(' ')
            val = None
        # print(ind, pointer[ind], cmd, var, val)
        if cmd == 'set':
            assign(ind, var, val)
        elif cmd == 'add':
            add(ind, var, val)
        elif cmd == 'mul':
            mul(ind, var, val)
        elif cmd == 'mod':
            mod(ind, var, val)
        elif cmd == 'snd':
            print(instruct)
            snd(ind, var, verbose=True)
        elif cmd == 'rcv':
            res = rcv(ind, var)
            if res is False:
                other_ind = get_other_ind(ind)
                if wait[other_ind] is True:
                    print(send_cnt)
                    return 0
                else:
                    print(f"set wait {ind} to True")
                    wait[ind] = True
                    ind = other_ind
                    # return 0
                    continue
        elif cmd == 'jgz':
            try:
                jump_var = int(var)
            except ValueError:
                jump_var = vars[ind][var]
            if jump_var > 0:
                try:
                    shift = int(val)
                except ValueError:
                    shift = vars[ind][val]
                pointer[ind] += shift
                continue
        else:
            raise ValueError(instruct)
        pointer[ind] += 1






if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("part", choices=["1", "2"], help="Which part you want to run, the first part or the second part")
    parser.add_argument("--sample", action="store_true", help="Do you want to use the sample input")

    args = parser.parse_args()

    input_file = "input.txt"
    if args.sample:
        input_file = "example_p2.txt"

    if args.part == "1":
        part1(input_file)
    else:
        part2(input_file)
