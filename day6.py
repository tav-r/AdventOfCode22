from sys import stdin


def find_markers(line, marker_size=4):
    # create char windows of required size
    quadruples = zip(*[line[i:] for i in range(marker_size)])

    # select indices of windows with number of different chars == marker_size
    markers = [
        j for (j, quadruple) in enumerate(quadruples, marker_size)
        if len(set(quadruple)) == marker_size
    ]

    # return first index
    return markers[0]


def main():
    line = stdin.readline()
    print(f"first marker: {find_markers(line.strip())}")
    print(f"first message: {find_markers(line.strip(), 14)}")


__name__ == "__main__" and main()
