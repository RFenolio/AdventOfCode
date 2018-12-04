from itertools import cycle
from typing import List

with open('day01_input.txt') as f:
	puzzle_input = f.readlines()
	puzzle_input = [int(num.strip()) for num in puzzle_input]
	# print(puzzle_input)

# Part 1
def frequency(input: List[int]) -> int:
	return sum(input)

part1 = frequency(puzzle_input)
print(f"Part 1: {part1}")

# Part 2
def frequency_repeat(input: List[int]) -> int:
	changes = cycle(input)
	frequency = 0
	frequencies = {0}
	for item in changes:
		frequency += item
		if frequency in frequencies:
			return frequency
		frequencies.add(frequency)


assert frequency_repeat([+1, -1]) == 0
assert frequency_repeat([+3, +3, +4, -2, -4]) == 10
assert frequency_repeat([-6, +3, +8, +5, -6]) == 5
assert frequency_repeat([+7, +7, -2, -7, -4]) == 14
part2 = frequency_repeat(puzzle_input)
print(f"Part 2: {part2}")