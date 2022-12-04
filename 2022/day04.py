import os
import sys

input_file = os.path.join(sys.path[0], "day04_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()

def parse_pairs(line):
    return [[int(val) for val in part.split('-')] for part in line.split(",")]

parsed_puzzle_input = [parse_pairs(line) for line in puzzle_input]

test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()
parsed_test = [parse_pairs(line) for line in test_input]

def fully_contains(pair):
    [a, b], [c, d] = pair
    if a == c or b == d:
        return True
    if a < c:
        return b > d
    else: 
        return b < d

def count_fully_contained(input):
    contained = [pair for pair in input if fully_contains(pair)]
    return len(contained)

assert(count_fully_contained(parsed_test) == 2)
print("Part 1:", count_fully_contained(parsed_puzzle_input))

def has_partial_overlap(pair):
    [a, b], [c, d] = pair
    if a == c or b == d:
        return True
    if a < c:
        return c <= b <= d
    else:
        return c <= a <= d

def count_overlap(input):
    overlap = [pair for pair in input if (fully_contains(pair) or has_partial_overlap(pair))]
    return len(overlap)

assert(count_overlap(parsed_test) == 4)
print("Part 2:", count_overlap(parsed_puzzle_input))






