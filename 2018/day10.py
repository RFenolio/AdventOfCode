from pprint import pprint

def parse_input(filename):
	with open(filename) as f:
		raw_input = f.read().splitlines()
	return [Point(line) for line in raw_input]

class Point:
	def __init__(self, raw):
		pos, vel = self._parse_raw(raw)
		self.px, self.py = pos
		self.vx, self.vy = vel

	@classmethod
	def _parse_raw(cls, input):
		input = input.strip('position=<')
		input = input.strip('>')
		pos, vel = input.split('> velocity=<')
		pos = [int(val) for val in pos.split(', ')]
		vel = [int(val) for val in vel.split(', ')]
		return pos, vel

	def move(self, times=1):
		self.px += (self.vx * times)
		self.py += (self.vy * times)

assert Point._parse_raw('position=< 9,  1> velocity=< 0,  2>') == ([9,1], [0,2])
test_point = Point('position=< 9,  1> velocity=< 0,  2>')
assert test_point.px == 9
assert test_point.py == 1
assert test_point.vx == 0
assert test_point.vy == 2
test_point.move()
assert test_point.px == 9
assert test_point.py == 3

def display_points(points, sizex=None, sizey=None):
	minx = min((p.px for p in points))
	maxx = max((p.px for p in points))
	miny = min((p.py for p in points))
	maxy = max((p.py for p in points))
	diffx = maxx-minx
	diffy = maxy-miny
	if (sizex is not None and diffx > sizex) or (sizey is not None and diffy > sizex):
		print(f"Grid is too large, sixe {diffx} x {diffy}, so not displaying")
		return
	grid = [[' ' for _ in range(maxx - minx + 1)] for _ in range(maxy-miny + 1)]
	for point in points:
		y = point.py - miny
		x = point.px - minx
		grid[y][x] = '#'
	for line in grid:
		print(''.join(line))

def move_points(points, times=1):
	for point in points:
		point.move(times=times)
	

test_points = parse_input('./day10_test_input.txt')

def move_and_render(points, time, start=0):
	print(f'called with {len(points)} points, time={time}, start={start}')
	move_points(points, times=start)
	for time in range(start, time):
		# for p in points[:2]:
			# print(p.px, p.py)
		print(f'At time {time}:\n')
		display_points(points, sizex=200, sizey=50)
		move_points(points)
		print('\n===================')
# move_and_render(test_points, 5, start=2)

# Part 1
points = parse_input('day10_input.txt')
move_and_render(points, 10832, start=10831)
