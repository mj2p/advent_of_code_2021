from day_2 import part_1, part_2


def test_part_1():
    movements = ["forward 1", "forward 3", "down 15", "up 3"]

    final = part_1(movements)

    assert final == 48


def test_part_2():
    movements = ["forward 1", "down 15", "up 3", "forward 3", "down 8", "forward 10"]

    """
    horizontal = 1 + 3 + 10 = 14
    depth = ((15-3) * 3) + ((15-3+8) * 10) = 236
    total = horizontal * depth = 3304
    """

    final = part_2(movements)

    assert final == 3304
