import os
import sys
import string
from itertools import islice

input_file = os.path.join(sys.path[0], "day03_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()

test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.splitlines()

def find_duplicate(rucksack):
    size = len(rucksack)
    return (set(rucksack[:size//2]).intersection(set(rucksack[size//2:]))).pop()
    
def get_priority(item):
    return string.ascii_letters.index(item) + 1

assert(get_priority('p') == 16)
assert(get_priority('L') == 38)
assert(get_priority('P') == 42)
assert(get_priority('v') == 22)
assert(get_priority('t') == 20)
assert(get_priority('s') == 19)

def calculate_priorities(input):
    return sum(get_priority(find_duplicate(rucksack)) for rucksack in input)

assert(calculate_priorities(test_input) == 157)
print("Part 1:", calculate_priorities(puzzle_input))

def chunk(items, chunk_size):
    items = iter(items)
    return iter(lambda: tuple(islice(items, chunk_size)), ())

test_groups = list(chunk(test_input, 3))

def get_badge(group):
    bags = [set(bag) for bag in group]
    return bags[0].intersection(*bags[0:]).pop()

print("Part 2:", sum(get_priority(get_badge(group)) for group in chunk(puzzle_input, 3)))