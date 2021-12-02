import collections
import itertools
import json
import os


def part_1(depths):
    """
    Calculate how many depth readings show an increase when compared to the previous in the list DEPTHS
    """
    current_depth = None
    increases = 0

    for depth in depths:
        if current_depth is None:
            current_depth = depth
            continue

        if depth > current_depth:
            increases += 1

        current_depth = depth

    return increases


def sliding_window(iterable, n):
    """
    yield the sum of the sliding window of 3 depths from the list DEPTHS
    """
    window = collections.deque(itertools.islice(iterable, n), maxlen=n)

    if len(window) == n:
        yield sum(window)

    for x in iterable:
        window.append(x)
        yield sum(window)


def part_2(depths):
    """
    Calculate the number of window sums that show an increase when compared to the previous
    """
    current_sum = None
    increases = 0

    for calc_sum in sliding_window(depths, 3):
        if current_sum is None:
            current_sum = calc_sum
            continue

        if calc_sum > current_sum:
            increases += 1

        current_sum = calc_sum

    return increases


if __name__ == "__main__":
    # expects json array of integers
    depth_data = json.load(open(os.path.join("data", "day_1.json")))

    part_1_final = part_1(depth_data)
    print("part_1", part_1_final)

    part_2_final = part_2(depth_data)
    print("part_2", part_2_final)
