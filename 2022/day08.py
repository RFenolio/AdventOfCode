import re
import os
import sys

input_file = os.path.join(sys.path[0], "day08_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()

example = """30373
25512
65332
33549
35390""".splitlines()

def parse_field(input):
    return [[int(height) for height in row] for row in input]

from pprint import pprint
pprint(parse_field(example))

foo = "abcde"
print(list(reversed(list(enumerate(foo)))))