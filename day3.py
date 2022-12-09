from sys import stdin


def priority(c):
    if c.islower():
        return ord(c) - ord("a") + 1

    return ord(c) - ord("A") + 27


def find_in_all(*comps):
    return [a for a in comps[0] if all(a in comp for comp in comps[1:])][0]


def rucksack_priority(rucksack):
    count = len(rucksack)
    comp1, comp2 = rucksack[count//2:], rucksack[:count//2]

    return priority(find_in_all(comp1, comp2))


def group_priority(memb1, memb2, memb3):
    return priority(find_in_all(memb1, memb2, memb3))


def main():
    rucksacks = [line.strip() for line in stdin.readlines() if line.strip()]

    part1 = sum(rucksack_priority(r) for r in rucksacks)
    print(part1)

    part2 = sum(
        group_priority(*rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)
    )
    print(part2)


if __name__ == "__main__":
    main()
