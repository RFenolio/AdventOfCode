dirtest1 = "R2, L3"
test_result1 = 5
dirtest2 = "R2, R2, R2"
test_result2 = 2
dirtest3 = "R5, L5, R5, R3"
test_result3 = 12
directions = "R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2"

def parse_directions(directions):
	return [ (x[0], int(x[1:])) for x in directions.split(', ')]

def find_distance(directions):
	x = 0
	y = 0
	facing = 0

	for direction in parse_directions(directions):
		if direction[0] == "R":
			facing = (facing + 1) % 4
		elif direction[0] == "L":
			facing = (facing - 1) % 4
		else:
			raise Exception("ERROR! That is not a valid turning direction")

		if facing == 0:
			y += direction[1]
		elif facing == 1:
			x += direction[1]
		elif facing == 2:
			y -= direction[1]
		elif facing == 3:
			x -= direction[1]
		else:
			raise Exception("ERROR! That is not a valid facing direction")

	return abs(x) + abs(y)

assert parse_directions(dirtest1) == [('R',2), ('L', 3)]

assert find_distance(dirtest1) == test_result1
assert find_distance(dirtest2) == test_result2
assert find_distance(dirtest3) == test_result3
print "The distance of Easter Bunny HQ in part 1:", find_distance(directions)

# part 2

def find_distance2(directions):
	x = 0
	y = 0
	facing = 0
	visited_locations = set([(0,0),])

	for direction in parse_directions(directions):
		# turn
		if direction[0] == "R":
			facing = (facing + 1) % 4
		elif direction[0] == "L":
			facing = (facing - 1) % 4
		else:
			raise Exception("ERROR! That is not a valid turning direction")

		# move
		if facing == 0:
			v = (0, 1)
		elif facing == 1:
			v = (1, 0)
		elif facing == 2:
			v = (0, -1)
		elif facing == 3:
			v = (-1, 0)
		else:
			raise Exception("ERROR! That is not a valid facing direction")

		for step in range(direction[1]):
			x += v[0]
			y += v[1]
			if (x, y) in visited_locations:
				return abs(x) + abs(y)
			else:
				visited_locations.add((x, y))



	return "Didn't visit any location twice!"

dirtest4 = "R8, R4, R4, R8"
test_result4 = 4
assert find_distance2(dirtest4) == test_result4

print "The distance of Easter Bunny HT in part 2:", find_distance2(directions)

