from sys import stdin
from itertools import chain, takewhile
from functools import reduce


def product(fs):
    return reduce(lambda x, y: x * y, fs, 1)

def transposed(forest):
    return [column for column in zip(*forest)]

def directions(i, j, forest):
    right = forest[i][j+1:]
    left = forest[i][:j][::-1]
    down = transposed(forest)[j][i+1:]
    up = transposed(forest)[j][:i][::-1]

    return right, left, down, up

def visible(i, j, forest):
    return any(
        # see if there is a higher tree in any direction
        max(direction) < forest[i][j] if direction else True
        for direction in directions(i, j, forest)
    )

def look(tree, direction):
    if not direction:
        return 0

    if direction[0] >= tree:
        return 1

    return 1 + look(tree, direction[1:])

def scenic_score(i, j, forest):
    distances = [
        look(forest[i][j], direction) for direction in directions(i, j, forest)
    ]

    scenic_score = product(distances)

    return scenic_score

def main():
    forest = [[int(c) for c in line.strip()] for line in stdin.readlines()
              if line.strip()]

    width, height = len(forest), len(forest[0])

    coords = [(i, j) for i in range(width) for j in range(height)]

    invisibles = [(i, j) for (i, j) in coords if not visible(i, j, forest)]

    print(f"{width * height - len(invisibles)} trees visible")

    scenic_scores = (scenic_score(i, j, forest) for (i, j) in coords)
    print(f"highest scenic score: {max(scenic_scores)}")


if __name__ == "__main__":
    main()
