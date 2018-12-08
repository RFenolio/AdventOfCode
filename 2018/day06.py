from pprint import pprint
def get_input(file):
	with open(file) as f:
		res = f.read().splitlines()
		return [[int(val) for val in item.split(', ')] for item in res]

puzzle_input = get_input('day06_input.txt')
test_input = get_input('day06_test.txt')
pprint(test_input)


a, b = zip(*puzzle_input)
# print(max(a), min(a))
# print(max(b), min(b))
# print(len(puzzle_input))
print(test_input)

def make_grid(puzzle_input):
	x, y = zip(*puzzle_input)
	print(x)
	print(y)
	max_x = max(x) + min(x)
	max_y = max(y) + min(y)
	grid = [[None for x in range(max_x)] for y in range(max_y)]
	return grid

def get_dist(a, b):
	x_dist = abs(a[0] - b[0])
	y_dist = abs(a[1] - b[1])
	return x_dist + y_dist
assert get_dist((0,0), (1, 3)) == 4
assert get_dist((1,2), (6,6)) == 9
assert get_dist((7,8), (1,10)) == 8

def closest_point(point, points):
	min_dist = 100000000000000
	closest_point = set([])
	for idx, item in enumerate(points):
		dist = get_dist(point, item)
		if dist < min_dist:
			min_dist = dist
			closest_point = set([idx])
		if dist == min_dist:
			closest_point.add(idx)
	return closest_point


def get_distances(puzz_input):
	grid = make_grid(puzz_input)
	for idx, y in enumerate(puzz_input):
		for x in range(len(y)):
			print(x, y)
			closest = closest_point((x, y), puzzle_input)
			print(closest)
			if len(closest) == 1:
				grid[y][x] = closest.pop()
			elif len(closest) > 1:
				grid[y][x] = '.'
			else:
				raise Exception('something went wrong')
	return grid

test_grid = get_distances(test_input)
pprint(test_grid)
