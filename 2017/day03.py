from itertools import cycle
from pprint import pprint

# --- Day 3: Spiral Memory ---

def cycle_distance(idx):
	x = 0
	y = 0
	dist = idx - 1
	leg_dist = 1

	def _add_x(x, y, leg_dist, val):
		x += val
		return x, y, leg_dist

	def _add_y(x, y, leg_dist, val):
		y += val
		leg_dist += 1
		return x, y, leg_dist

	def _sub_x(x, y, leg_dist, val):
		x -= val
		return x, y, leg_dist

	def _sub_y(x, y, leg_dist, val):
		y -= val
		leg_dist += 1
		return x, y, leg_dist

	funcs = cycle([_add_x, _add_y, _sub_x, _sub_y])
	while dist > 0:
		func = funcs.next()
		next_dist = dist - leg_dist
		x, y, leg_dist = func(x, y, leg_dist, min(dist, leg_dist))
		dist = next_dist

	return abs(x) + abs(y)

assert cycle_distance(1) == 0
assert cycle_distance(12) == 3
assert cycle_distance(23) == 2
assert cycle_distance(1024) == 31

print "Part 1 solution:", cycle_distance(312051)

# --- Part Two ---

from math import sqrt, ceil, floor

def make_grid(total):
	size = ceil(sqrt(total)) + 3
	return [[0 for x in range(int(size))] for y in range(int(size))]

def calculate_cell(grid, x, y):
	# pprint(grid)
	# print x, y
	vals = [
		grid[x][y + 1],
		grid[x][y - 1],
		grid[x + 1][y],
		grid[x + 1][y + 1],
		grid[x + 1][y - 1],
		grid[x - 1][y],
		grid[x - 1][y + 1],
		grid[x - 1][y - 1],
	]
	# print vals
	# print "======================================="
	return sum(vals)

test_grid = [
	[1, 2, 3],
	[4, 0, 5],
	[6, 7, 8],
]
assert calculate_cell(test_grid, 1, 1) == 36

def update_cell(grid, x, y):
	grid[x][y] = calculate_cell(grid, x, y)

def spiral_memory(max_val):
	grid = make_grid(100)
	x = len(grid)/2
	y = len(grid)/2
	grid[x][y] = 1
	leg = 1
	dist = 100 - 1
	
	def _move_left(grid, x, y, leg, val):
		for _ in range(val):
			x += 1
			update_cell(grid, x, y)
			if grid[x][y] > max_val:
				break
		return x, y, leg

	def _move_up(grid, x, y, leg, val):
		for _ in range(val):
			y += 1
			update_cell(grid, x, y)
			if grid[x][y] > max_val:
				break
		leg += 1
		return x, y, leg

	def _move_right(grid, x, y, leg, val):
		for _ in range(val):
			x -= 1
			update_cell(grid, x, y)
			if grid[x][y] > max_val:
				break
		return x, y, leg

	def _move_down(grid, x, y, leg, val):
		for _ in range(val):
			y -= 1
			update_cell(grid, x, y)
			if grid[x][y] > max_val:
				break
		leg += 1
		return x, y, leg

	funcs = cycle([_move_left, _move_up, _move_right, _move_down])

	while dist > 0:
		func = funcs.next()
		next_dist = dist - leg
		x, y, leg = func(grid, x, y, leg, min(dist, leg))
		dist = next_dist
		if grid[x][y] > max_val:
				break

	return grid[x][y]


print "Part 2 solution:", spiral_memory(312051)





