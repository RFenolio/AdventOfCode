with open('day11_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read()

def parse_input(puzzle_input):
	return puzzle_input.split(',')


def move(start, direction):
	return [sum(x) for x in zip(start, direction)]

assert move([1, 2, 3], [2, 3, 4]) == [3, 5, 7]

DIRECTIONS = {
	'n': (0, +1, -1),
	'ne': (+1,  0, -1),
	'se': (+1, -1,  0),
	's': (0, -1, +1),
	'sw': (-1,  0, +1),
	'nw': (-1, +1,  0),
}

def distance_from_origin(coords):
	return max(abs(x) for x in coords)

def walk(puzzle_input):
	location = (0, 0, 0)
	steps = parse_input(puzzle_input)
	max_distance = 0
	for step in steps:
		location = move(location, DIRECTIONS[step])
		current_dist = distance_from_origin(location)
		max_distance = max([current_dist, max_distance]) 
	return current_dist, max_distance

test1 = 'ne,ne,ne'
test2 = 'ne,ne,sw,sw'
test3 = 'ne,ne,s,s'
test4 = 'se,sw,se,sw,sw'

assert walk(test1)[0] == 3
assert walk(test2)[0] == 0
assert walk(test3)[0] == 2
assert walk(test4)[0] == 3

print "Part 1, 2 solution:", walk(puzzle_input)