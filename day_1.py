import collections
import itertools
import json
import os

DEPTHS = json.load(open(os.path.join('data', 'day_1.json')))


def part_1():
    current_depth = None
    increases = 0

    for depth in DEPTHS:
        if current_depth is None:
            # print('no previous depth')
            current_depth = depth
            continue

        # print(depth, ('increased' if depth > current_depth else 'decreased'))

        if depth > current_depth:
            increases += 1

        current_depth = depth

    print(increases)


def sliding_window(iterable, n):
    window = collections.deque(itertools.islice(iterable, n), maxlen=n)

    if len(window) == n:
        yield sum(window)

    for x in iterable:
        window.append(x)
        yield sum(window)


def part_2():
    current_sum = None
    increases = 0

    for calc_sum in sliding_window(DEPTHS, 3):
        if current_sum is None:
            # print('no previous sum')
            current_sum = calc_sum
            continue

        # print(calc_sum, calc_sum > current_sum)

        if calc_sum > current_sum:
            increases += 1

        current_sum = calc_sum

    print(increases)


if __name__ == '__main__':
    part_1()
    part_2()
