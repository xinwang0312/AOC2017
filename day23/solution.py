import argparse
import itertools
import os
import re
from collections import defaultdict, Counter
from pprint import pprint


def part1(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    variables = {reg: 0 for reg in 'abcdefgh'}

    def assign(var, val):
        try:
            variables[var] = int(val)
        except ValueError:
            variables[var] = variables[val]

    def sub(var, val):
        try:
            variables[var] -= int(val)
        except ValueError:
            variables[var] -= variables[val]

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
    j = 0
    num_mul = 0
    while i < len(lines):
        instruct = lines[i]
        cmd, var, val = instruct.split(' ')
        j += 1
        print(i, cmd, var, val)
        if cmd == 'set':
            assign(var, val)
        elif cmd == 'add':
            add(var, val)
        elif cmd == 'sub':
            sub(var, val)
        elif cmd == 'mul':
            mul(var, val)
            num_mul += 1
        elif cmd == 'mod':
            mod(var, val)
        elif cmd == 'jnz':
            try:
                jump_var = int(var)
            except ValueError:
                jump_var = variables[var]
            print(f'{var} = {jump_var}')
            if jump_var != 0:
                try:
                    shift = int(val)
                except ValueError:
                    shift = variables[val]
                i += shift
                continue
        else:
            raise ValueError(instruct)
        i += 1
    print(f"{num_mul=}")




def part2_test(input_file):
    with open(input_file) as f:
        lines = [x.strip() for x in f.read().strip().split("\n")]
    variables = {reg: 0 for reg in 'abcdefgh'}
    variables['a'] = 1

    # lines[8] = "set f 0"  # b is 109300 at that time 


    def assign(var, val):
        try:
            variables[var] = int(val)
        except ValueError:
            variables[var] = variables[val]

    def sub(var, val):
        try:
            variables[var] -= int(val)
        except ValueError:
            variables[var] -= variables[val]

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
    j = 0
    while i < len(lines):
        if i == 8: print(variables); return 
        instruct = lines[i]
        cmd, var, val = instruct.split(' ')
        j += 1
        print(i, cmd, var, val)
        if cmd == 'set':
            assign(var, val)
        elif cmd == 'add':
            add(var, val)
        elif cmd == 'sub':
            sub(var, val)
        elif cmd == 'mul':
            mul(var, val)
        elif cmd == 'mod':
            mod(var, val)
        elif cmd == 'jnz':
            # if i in [19, 23]: i+=1; continue
            try:
                jump_var = int(var)
            except ValueError:
                jump_var = variables[var]
            print(f'{var} = {jump_var}')
                
            if i == 14:
                print(f"b = {variables['b']}")
            if jump_var != 0:
                try:
                    shift = int(val)
                except ValueError:
                    shift = variables[val]
                i += shift
                continue
        else:
            raise ValueError(instruct)
        i += 1
        if j > 80:
            print(variables)
            return 0
#     
    print(variables)

def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False
         
    return [2]+[i for i in range(3,n,2) if sieve[i]]


def part2(input_file):
    """
    There are three layers of loops:
        1. the most outer layer loops b from 109300 to 126300 by increasing 17 (by running the bf and break till Ln 8)
        2. for every b, d increases from 2 to b by 1
        3. for each d, e increases from 2 to b by 1
    for every outer loop #1, h increases by 1 except when d * e - b = 0 (ln 15 set f to 0, ln 24 jumps over adding h if f is 0)

    there are 1001 loops in #1, and only 911 of them have b which is not a prime number, i.e., there exist d and e such that d * e = b, which will not increase h
    """
    b = range(109300, 126300 + 1, 17)
    print(len(b), max(b))
    res = []
    remove = primes(126300)
    print(len(remove))
    print(len(set(b) - set(remove)))

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
