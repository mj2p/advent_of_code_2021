import json
import os


def part_1(movements):
    """
    Determine the final horizontal and depth from the list of MOVEMENTS
    `forward` increases horizontal.
    `down` increases depth
    `up` decreases depth
    return: horizontal * depth
    """
    horizontal = depth = 0

    for movement in movements:
        movement_parts = movement.split(" ")

        if movement_parts[0] == "forward":
            horizontal += int(movement_parts[1])

        if movement_parts[0] == "down":
            depth += int(movement_parts[1])

        if movement_parts[0] == "up":
            depth -= int(movement_parts[1])

    return horizontal * depth


def part_2(movements):
    """
    Calculate final position considering down and up commands adjust your `aim`
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
    """
    horizontal = depth = aim = 0

    for movement in movements:
        movement_parts = movement.split(" ")

        if movement_parts[0] == "forward":
            horizontal += int(movement_parts[1])

            if aim != 0:
                depth += int(movement_parts[1]) * aim

        if movement_parts[0] == "down":
            aim += int(movement_parts[1])

        if movement_parts[0] == "up":
            aim -= int(movement_parts[1])

    return horizontal * depth


if __name__ == "__main__":
    # expects json array of strings eg. ['forward 2', 'down 3', ...]
    movements_data = json.load(open(os.path.join("data", "day_2.json")))

    part_1_final = part_1(movements_data)
    print("part_1", part_1_final)

    part_2_final = part_2(movements_data)
    print("part_2", part_2_final)
