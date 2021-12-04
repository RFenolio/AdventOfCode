from collections import Counter
import os
import sys

"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day03_input.txt")
with open(input_file) as f:
    puzzle_input = f.read().splitlines()

test_input_file = os.path.join(sys.path[0], "day03_test_input.txt")
with open(test_input_file) as f:
    puzzle_test_input = f.read().splitlines()

"""
Part 1
"""
counts = [Counter(items).most_common() for items in zip(*puzzle_input)]
gamma = int("".join([c[0][0] for c in counts]), 2)
epsilon = int("".join([c[-1][0] for c in counts]), 2)
print("Part 1:", gamma * epsilon)

"""
Part 2
"""
def get_o2(input):
    o2_vals = input.copy()
    for idx in range(len(o2_vals[0])):
        if len(o2_vals) == 1:
            print("o2 last idx:", idx)
            break
        counts = Counter([num[idx] for num in o2_vals]).most_common()
        # derault to 1 if equal
        if counts[0][1] == counts[1][1]:
            o2_vals = [num for num in o2_vals if num[idx] == "1"]
        else:
            o2_vals = [num for num in o2_vals if num[idx] == counts[0][0]]
    return int(o2_vals[0], 2)

assert get_o2(puzzle_test_input) == 23

def get_co2(input):
    co2_vals = input.copy()
    for idx in range(len(co2_vals[0])):
        if len(co2_vals) == 1:
            print("co2 last idx:", idx)
            break
        counts = Counter([num[idx] for num in co2_vals]).most_common()
        # derault to 0 if equal
        if counts[0][1] == counts[1][1]:
            co2_vals = [num for num in co2_vals if num[idx] == "0"]
        else:
            co2_vals = [num for num in co2_vals if num[idx] == counts[-1][0]]
    return int(co2_vals[0], 2)

assert get_co2(puzzle_test_input) == 10

co2 = get_co2(puzzle_input)
o2 = get_o2(puzzle_input)
print("Part 2:", co2 * o2)