from sys import stdin
from functools import reduce


steps = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def apply_step(pos, step):
    return (pos[0] + step[0], pos[1] + step[1])


def diagonal(pos1, pos2):
    return all(abs(pos1[i] - pos2[i]) == 1 for i in (0, 1))


def neighbor(pos1, pos2):
    return sum(abs(pos1[i] - pos2[i]) for i in (0, 1)) == 1


def follow(h_pos, t_poss):
    if not t_poss:
        return []

    t_pos = t_poss[0]

    if h_pos == t_pos or neighbor(h_pos, t_pos)\
       or diagonal(t_pos, h_pos):
        new_t_pos = t_pos
    else:
        t_i, t_j = t_pos
        h_i, h_j = h_pos

        # go one step in each dimension in which head is different
        i, j = (
            d // abs(d) if d else 0
            for d in [h_i - t_i, h_j - t_j]
        )

        new_t_pos = (t_i + i, t_j + j)

    return [new_t_pos] + follow(new_t_pos, t_poss[1:])


def step_and_follow(direction, h_pos, t_poss):
    new_h_pos = apply_step(h_pos, steps[direction])

    tails = follow(new_h_pos, t_poss)

    return new_h_pos, tails


def move_and_follow(movement, h_pos, t_poss):
    direction, count_str = movement

    # apply the steps "int(count_str)" times, starting at the current position,
    #  using reduce
    return reduce(
        lambda poss, _: poss + [step_and_follow(direction, *poss[-1])],
        range(int(count_str)),
        [(h_pos, t_poss)]
    )[1:]


def process_moves(moves, head_start, tails_starts):
    # apply all moves, starting with the current position using reduce
    return zip(*reduce(
        lambda poss, move: poss + move_and_follow(move, *poss[-1]),
        moves,
        [(head_start, tails_starts)]
    ))


def main():
    moves = [tuple(line.strip().split(" ")) for line in stdin.readlines()
             if line.strip()]

    # first part is with a tail length of 1
    _, history_tail1 = process_moves(moves, (0, 0), [(0, 0)])

    print(len(set(h[-1] for h in history_tail1)))

    # second with a tail length of 10
    _, history_tail2 = process_moves(moves, (0, 0), [(0, 0) for _ in range(9)])

    print(len(set(h[-1] for h in history_tail2)))


if __name__ == "__main__":
    main()
