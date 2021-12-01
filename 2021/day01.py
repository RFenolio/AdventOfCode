from math import inf
import os
import sys

input_file = os.path.join(sys.path[0], "day01_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()
	puzzle_input = [int(val) for val in puzzle_input]


# Part 1
increases = 0
for idx, val in enumerate(puzzle_input):
	if idx == 0:
		continue
	if val > puzzle_input[idx-1]:
		increases +=1

print("Part 1: ", increases)

# Part 2
prev = inf
increases2 = 0
for idx, val in enumerate(puzzle_input):
	current = sum(puzzle_input[idx:idx+3])
	if current > prev:
		increases2 += 1
	prev = current

print("Part 2: ", increases2)