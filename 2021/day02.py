import os
import sys

input_file = os.path.join(sys.path[0], "day02_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()


# Part 1
distance = 0
depth = 0
for line in puzzle_input:
	direction, dist = line.split(" ")
	dist = int(dist)
	if direction == "forward":
		distance += dist
	elif direction == "down":
		depth += dist
	elif direction == "up":
		depth -= dist
print("Part 1:")
print("distance:", distance)
print("depth:", depth)
print("solution:", distance * depth)

# Part 2

distance = 0
depth = 0
aim = 0
for line in puzzle_input:
	direction, dist = line.split(" ")
	dist = int(dist)
	if direction == "forward":
		distance += dist
		depth += aim * dist
	elif direction == "down":
		aim += dist
	elif direction == "up":
		aim -= dist

print("Part 2:")
print("distance:", distance)
print("depth:", depth)
print("solution:", distance * depth)