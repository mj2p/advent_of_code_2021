from day_3 import part_1, part_2


def test_part_1():
    diagnostics = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    final = part_1(diagnostics)

    assert final == 198


def test_part_2():
    diagnostics = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    final = part_2(diagnostics)

    assert final == 230
