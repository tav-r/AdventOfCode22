from sys import stdin

ELFS, YOUS = "ABC", "XYZ"

def choose(elf, outcome):
    outcome_map = "YZX"

    return YOUS[(ELFS.find(elf) + outcome_map.find(outcome)) % 3]

def points(elf, you):
    value_you = YOUS.find(you)
    value_elf = ELFS.find(elf)

    return [3, 6, 0][value_you - value_elf] + value_you + 1

def main():
    instrs = [line.strip()[::2] for line in stdin.readlines() if line.strip()]

    games1 = [points(*instr) for instr in instrs]
    print(f"total points (part 1): {sum(games1)}")

    games2 = [points(instr[0], choose(*instr)) for instr in instrs]
    print(f"total points (part 2): {sum(games2)}")


if __name__ == "__main__":
    main()
