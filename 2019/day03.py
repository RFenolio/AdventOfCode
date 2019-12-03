with open("day03_input.txt") as f:
	w1, w2 = [dirs.split(',') for dirs in f.readlines()]

dirs = {
	"L": (0, 1),
	"R": (0, -1),
	"U": (1, 0),
	"D": (-1, 0),
}
def parse_direction(dir):
	return (dir[0], int(dir[1:]))

def make_wire(directions):
	current = (0, 0)
	locs = set()
	for direction in directions:
		d, dist = parse_direction(direction)
		move = dirs[d]
		for _ in range(dist):
			current = (current[0] + move[0], current[1] + move[1])
			locs.add(current)
	return locs

assert make_wire(["L2", "U3"]) == set([(0, 1), (0, 2), (1, 2), (2, 2), (3, 2)])

def find_closest_intersection(w1, w2):
	return min(abs(a) + abs(b) for a, b in w1.intersection(w2))

# --- Day 3: Crossed Wires ---

t1_1 = make_wire("R8,U5,L5,D3".split(","))
t1_2 = make_wire("U7,R6,D4,L4".split(","))
assert find_closest_intersection(t1_1, t1_2) == 6

t2_1 = make_wire("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","))
t2_2 = make_wire("U62,R66,U55,R34,D71,R55,D58,R83".split(","))
assert find_closest_intersection(t2_1, t2_2) == 159

t3_1 = make_wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","))
t3_2 = make_wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","))
assert find_closest_intersection(t3_1, t3_2) == 135

wire1 = make_wire(w1)
wire2 = make_wire(w2)
part1_solution = find_closest_intersection(wire1, wire2)
print("Part 1:", part1_solution)

# --- Part Two ---

def make_wire_with_distance(directions):
	current = (0, 0)
	locs = []
	dist = 0
	for direction in directions:
		d, dist = parse_direction(direction)
		move = dirs[d]
		for _ in range(dist):
			current = (current[0] + move[0], current[1] + move[1])
			locs.append(current)
	return locs

def find_shortest_intersection(w1, w2):
	intersections = set(w1).intersection(set(w2))
	distances = ((w1.index(elem), w2.index(elem)) for elem in intersections)
	return min(a + b + 2 for a, b in distances)

t4_1 = make_wire_with_distance("R8,U5,L5,D3".split(","))
t4_2 = make_wire_with_distance("U7,R6,D4,L4".split(","))
assert find_shortest_intersection(t4_1, t4_2) == 30

t5_1 = make_wire_with_distance("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","))
t5_2 = make_wire_with_distance("U62,R66,U55,R34,D71,R55,D58,R83".split(","))
assert find_shortest_intersection(t5_1, t5_2) == 610

t6_1 = make_wire_with_distance("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","))
t6_2 = make_wire_with_distance("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","))
assert find_shortest_intersection(t6_1, t6_2) == 410

wire1_dist = make_wire_with_distance(w1)
wire2_dist = make_wire_with_distance(w2)
part2_solution = find_shortest_intersection(wire1_dist, wire2_dist)
print("Part 2:", part2_solution)
