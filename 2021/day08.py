import os
import sys
from itertools import chain
from collections import defaultdict

"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day08_input.txt")
with open(input_file) as f:
    puzzle_input = f.read().splitlines()

input_file = os.path.join(sys.path[0], "day08_test_input.txt")
with open(input_file) as f:
    test_puzzle_input = f.read().splitlines()

def parse_input(input):
    return [parse_line(line) for line in input]

def parse_line(line: str):
    signal_pattern, output = line.split(" | ")
    return signal_pattern.split(), output.split()

test_input = parse_input(test_puzzle_input)
test_single_line = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
test_single_line = parse_line(test_single_line)
puzzle = parse_input(puzzle_input)

"""
Part 1
"""
def count_uniques(input):
    _, outputs = zip(*input)
    return len([pattern for pattern in chain.from_iterable(outputs) if len(pattern) in {2, 3, 4, 7}])

assert count_uniques(test_input) == 26
print("Part 1:", count_uniques(puzzle))

"""
Part 2
"""
def group_codes_by_len(line):
    codes = defaultdict(list)
    segments, _ = line
    for code in segments:
        codes[len(code)].append(set(code))
    return codes

def make_key(line):
    """
    number variables represent sets of segments in screen of that number
    """
    codes = group_codes_by_len(line)
    one  = codes[2][0]
    four  = codes[4][0]
    seven  = codes[3][0]
    eight = codes[7][0]
    len_five = codes[5].copy()
    len_six = codes[6].copy()
    three = [num for num in len_five if one.issubset(num)][0]
    len_five.remove(three)
    nine = [num for num in len_six if three.issubset(num)][0]
    len_six.remove(nine)
    five = [val for val in len_five if val.issubset(nine)][0]
    len_five.remove(five)
    two = len_five[0]
    zero = [num for num in len_six if one.issubset(num)][0]
    len_six.remove(zero)
    six = len_six[0]

    return {
    "".join(sorted(zero)): '0',
    "".join(sorted(one)): '1',
    "".join(sorted(two)): '2',
    "".join(sorted(three)): '3',
    "".join(sorted(four)): '4',
    "".join(sorted(five)): '5',
    "".join(sorted(six)): '6',
    "".join(sorted(seven)): '7',
    "".join(sorted(eight)): '8',
    "".join(sorted(nine)): '9',
    }

def make_num_from_output(line):
    _, output = line
    key = make_key(line)
    vals = [key["".join(sorted(val))] for val in output]
    return int("".join(vals))

assert make_num_from_output(test_single_line) == 5353
assert sum(make_num_from_output(line) for line in test_input) == 61229
print("Part 2:", sum(make_num_from_output(line) for line in puzzle))
