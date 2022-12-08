from functools import reduce
from sys import stdin


def update(calories, line):
    if line:
        return [calories[0] + int(line)] + calories[1:]
    return [0] + calories


def main():
    lines = [line.strip() for line in stdin.readlines()]

    calories = sorted(reduce(update, lines, [0]), reverse=True)

    print(f"max: {calories[0]}")
    print(f"top three: {sum(calories[i] for i in range(3))}")


__name__ == '__main__' and main()
