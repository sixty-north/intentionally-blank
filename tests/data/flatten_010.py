mixed = [
    [
        [17, 22, 22, 15, 15, 21, 22, 19, 17, 21, 22, 19],
        [20, 20, 22, 18, 20, 17, 21, 18, 22, 17, 18, 22],
        14,
        [22, 19, 20, 22, 21, 20, 19, 18, 15, 19, 22, 19],
        [19, 20, 17, 15, 18, 22, 15, 17, 16, 22, 19, 20]
    ],
    23,
    [21, 25, 28, 23, 22, 22, 22],
    [18, 13, 14, 18, 16, 14, 15],
    [
        [12, 14, 13, 13],
        [11, 14, 17],
    ],
    [18, 17, 17, 16, 12, 10, 11],
    15,
    17,
]


def flatten(items):
    return []  # TODO!


if __name__ == "__main__":
    result = flatten(mixed)

    print(result)

    assert result == [
        17, 22, 22, 15, 15, 21, 22, 19, 17, 21, 22, 19,
        20, 20, 22, 18, 20, 17, 21, 18, 22, 17, 18, 22,
        14,
        22, 19, 20, 22, 21, 20, 19, 18, 15, 19, 22, 19,
        19, 20, 17, 15, 18, 22, 15, 17, 16, 22, 19, 20,
        23,
        21, 25, 28, 23, 22, 22, 22,
        18, 13, 14, 18, 16, 14, 15,
        12, 14, 13, 13,
        11, 14, 17,
        18, 17, 17, 16, 12, 10, 11,
        15,
        17,
    ]
