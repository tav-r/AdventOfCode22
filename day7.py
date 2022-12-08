from sys import stdin
from collections import defaultdict
from itertools import takewhile
from functools import reduce
from pprint import pprint


def file_or_dir(line):
    if line.startswith("dir"):
        return (line.split(" ")[1], [])

    size_str, name = line.split(" ")
    return (name, int(size_str))


def get_contents(lines):
    dirlist = dict(
        file_or_dir(line) for line in takewhile(
            lambda s: not s.startswith("$"), lines
        )
    )

    return dirlist, lines[len(dirlist):]


def process_lines(dirname, lines):
    contents = dict()

    while True:
        if not lines or lines[0] == "$ cd ..":
            return contents, lines[1:]
        elif lines[0] == "$ ls":
            contents, lines = get_contents(lines[1:])
        else:
            dirname = lines[0].split(" ")[2]
            contents[dirname], lines = process_lines(dirname, lines[1:])

    raise ValueError("bad input")


def dir_tree_size(dir_tree):
    def size(val):
        if isinstance(val, int):
            return val
        else:
            return dir_tree_size(val)

    return sum(size(e) for (_, e) in dir_tree.items())


def all_sizes(name, dir_tree):
    return [(name, dir_tree_size(dir_tree))] +\
        [name_size for (name, val) in dir_tree.items() if isinstance(val, dict)
         for name_size in all_sizes(name, val)]


def main():
    lines = [line.strip() for line in stdin.readlines() if line.strip()]

    dir_tree, _ = process_lines("/", lines[1:])

    dir_sizes = all_sizes("/", dir_tree)

    # part one

    max_size = 100000
    sum_max_size = sum(size for (name, size) in dir_sizes if size <= max_size)

    print(f"size of all directories smaller than {max_size} is {sum_max_size}")

    # part two
    total_space = 70000000
    space_needed = 30000000
    space_used = dir_tree_size(dir_tree)
    space_free = total_space - space_used
    big_enough = [
        (n, s) for (n, s) in dir_sizes if space_free + s >= space_needed
    ]

    name, size = min(big_enough, key=lambda x: x[1])
    available_new = total_space - space_used + size
    print(f"delete folder{name} with size {size} since {total_space}-"
          f"{space_used}+{size}={available_new}")


if __name__ == "__main__":
    main()
