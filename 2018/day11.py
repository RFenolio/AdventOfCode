from itertools import chain

with open('day11_input.txt') as f:
	puzzle_input = f.read().splitlines()

def rack_id(x):
	return x + 11

def power_level(x, y, serial):
	x += 1
	y += 1
	rack_id = x + 10
	power = rack_id * y
	power += serial
	power *= rack_id
	hundreds = ((power // 10) // 10) % 10
	return hundreds - 5

assert power_level(2, 4, 8) == 4
assert power_level(121,78, 57) == -5
assert power_level(100,152, 71) == 4
assert power_level(216,195, 39) == 0

test_grid = [
	[-2,-4, 4,  4, 4],
	[-4 ,  4,   4,   4,  -5],
 	[4,   3,   3,   4,  -4],
 	[1,   1,  2,  4,  -3],
	[-1,   0,   2,  -5,  -2],
]

def get_square(grid, y, x, size=3):
	res = []
	for y in range(y, y+size):
		res.extend(grid[y][x:x+size])
	return sum(res)

assert get_square(test_grid, 1, 1) == 29

def make_grid(serial, size=300):
	return [[power_level(x, y, serial) for x in range(size)]for y in range(size)]

def max_power(serial, size=300):
	grid = make_grid(serial, size)
	mp = -9999999999999999
	mx = None
	my = None
	# print(grid[44][32])
	# print(get_square(grid, 44, 32))
	for x in range(size - 3):
		for y in range(size - 3):
			score = get_square(grid, x, y)
			if score > mp:
				mp = score
				mx = x
				my = y
	return mp, my+1, mx+1

test_18 = max_power(18)


test_42 = max_power(42)
# Part 1
serial = 3613
part1 = max_power(serial)
print(f'Part 1: x coord is {part1[1]}, y coord is {part1[2]}')



def max_power2(grid, size):
	mp = -9999999999999999
	mx = None
	my = None
	grid_size = len(grid)
	for x in range(300 - size):
		for y in range(300 - size):
			# print(x, y, size)
			score = get_square(grid, x, y, size)
			if score > mp:
				mp = score
				mx = x
				my = y
	return mp, my+1, mx+1

def adjustable(serial):
	grid = make_grid(serial)
	mp = 0
	max_box = None
	max_res = None
	for box in range(2, 20):
		res = max_power2(grid, box)
		if res[0] > mp:
			mp = res[0]
			max_res = res
			max_box = box
	return max_box, max_res

	

print(adjustable(serial))
