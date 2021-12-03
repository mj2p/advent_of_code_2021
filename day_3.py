import json
import os
from collections import Counter
from typing import List


def get_common_bits(diagnostics, index, override_equal=False):
    bits = []

    for diag in diagnostics:
        bits.append(diag[index])

    c = Counter(bits)

    if override_equal and len(c.most_common()) > 1:
        if c.most_common()[0][1] == c.most_common()[1][1]:
            return "1", "0"

    common = c.most_common()[0][0]
    not_common = "0" if common == "1" else "1"

    return common, not_common


def part_1(diagnostics):
    """
    Calculate Gamma and Epsilon values from diagnostics
    Gamma and Epsilon are binary numbers to be converted to decimal
    Gamma = most common bits from disagnostics
    Epsilon = least common
    """
    most_common_bits = []
    least_common_bits = []

    for x in range(len(diagnostics[0])):
        most_common, least_common = get_common_bits(diagnostics, x)
        most_common_bits.append(most_common)
        least_common_bits.append(least_common)

    gamma_bin = "".join(most_common_bits)
    epsilon_bin = "".join(least_common_bits)

    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)

    return gamma * epsilon


def filter_numbers_by_bits(numbers: List, index: int, num_filter: int):
    if len(numbers) == 1:
        return numbers

    output = []

    for num in numbers:
        if int(num[index]) != num_filter:
            continue
        output.append(num)

    return output


def part_2(diagnostics):
    """
    Calculate Oxygen Generator Rating and CO2 scrubber rating
    O2 Gen - keep only numbers that contain the most common bit in each location
    CO2 scrub - same but least common
    """
    oxygen_generator_rating = co2_scrubber_rating = diagnostics

    for x in range(len(diagnostics[0])):
        o2_most_common, o2_least_common = get_common_bits(
            oxygen_generator_rating, x, override_equal=True
        )
        co2_most_common, co2_least_common = get_common_bits(
            co2_scrubber_rating, x, override_equal=True
        )
        oxygen_generator_rating = filter_numbers_by_bits(
            oxygen_generator_rating, x, int(o2_most_common)
        )
        co2_scrubber_rating = filter_numbers_by_bits(
            co2_scrubber_rating, x, int(co2_least_common)
        )

    oxygen_generator_rating = int(oxygen_generator_rating[0], 2)
    co2_scrubber_rating = int(co2_scrubber_rating[0], 2)

    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    # expects json array of integers
    diagnostic_data = json.load(open(os.path.join("data", "day_3.json")))

    part_1_final = part_1(diagnostic_data)
    print("part_1", part_1_final)

    part_2_final = part_2(diagnostic_data)
    print("part_2", part_2_final)
