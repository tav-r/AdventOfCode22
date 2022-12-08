"""Advent of Code, day 5"""
from sys import stdin
from functools import reduce, partial
from copy import copy

def get(row, n, stacks):
    res = stacks[row-1][:n]
    stacks[row-1] = stacks[row-1][n:]

    return res, stacks

def put9000(row, cargos, stacks):
    stacks[row-1] = cargos[::-1] + stacks[row-1]

    return stacks

def put9001(row, cargos, stacks):
    stacks[row-1] = cargos + stacks[row-1]

    return stacks

def move(stacks, move_desc, put=put9000):
    num, src, dst = move_desc
    return put(dst, *get(src, num, stacks))

def main():
    # read all input lines
    lines = list(stdin.readlines())

    # parse stacks (transposed)
    stacks_t = [line[1::4] for line in lines if "[" in line]

    # transpose transposed stacks
    stacks_init = [list(c for c in r if c.strip()) for r in zip(*stacks_t)]

    # parse all moves
    moves = [
        list(int(i) for i in list(line.split(" "))[1::2])
        for line in lines if line.startswith("move")
    ]

    # make moves with CrateMover 9000 (first part)
    stacks9000 = reduce(move, moves, copy(stacks_init))

    # make moves with CrateMover 9001 (second part)
    stacks9001 = reduce(partial(move, put=put9001), moves, copy(stacks_init))

    # print top crates
    print("".join(s[0] for s in stacks9000 if s))
    print("".join(s[0] for s in stacks9001 if s))


__name__ == "__main__" and main()
