from day_1 import part_1, part_2


def test_part_1():
    depths = [1, 2, 3, 2, 3, 2, 3]

    final = part_1(depths)

    assert final == 4


def test_part_2():
    depths = [1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 1]

    """
    triplets:
    1+1+1 = 3
    1+1+2 = 4 True
    1+2+2 = 5 True
    2+2+2 = 6 True
    2+2+3 = 7 True
    2+3+3 = 8 True
    3+3+2 = 8 False
    3+2+2 = 7 False
    2+2+1 = 5 False
    """

    final = part_2(depths)

    assert final == 5
