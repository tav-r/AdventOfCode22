from sys import stdin


def one_contains_other(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    return r1[0] <= r2[0] and r2[1] <= r1[1] or\
        r2[0] <= r1[0] and r1[1] <= r2[1]


def overlap(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    a, b = r1
    c, d = r2

    return any(i in range(c, d+1) for i in range(a, b+1))

def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    (a, b), (c, d) = ((int(i) for i in p.split("-")) for p in line.split(","))
    return (a, b), (c, d)


def main() -> None:
    pairs = [parse_line(line) for line in stdin.readlines() if line.strip()]

    contained = [
        pair for pair in pairs if one_contains_other(*pair)
    ]

    print(f"number of fully contained ranges: {len(contained)}")

    overlapping = [
        pair for pair in pairs if overlap(*pair)
    ]

    print(f"number of overlapping ranges: {len(overlapping)}")


if __name__ == "__main__":
    main()
