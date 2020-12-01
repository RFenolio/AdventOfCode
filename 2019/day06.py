
with open("day06_input.txt") as f:
	data = f.read()

def parse_data(raw_data):
	return [pair.split(")") for pair in raw_data.split('\n')]

def make_graph(data):
	return {body: parent for parent, body in data}

test_data = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''

test_data = parse_data(test_data)
test_graph = make_graph(test_data)

def count_orbits(obj, graph):
	if obj == "COM":
		return 0
	else:
		return count_orbits(graph[obj], graph) + 1

def count_all_orbits(graph):
	total = 0
	for obj in graph:
		total += count_orbits(obj, graph)
	return total

assert count_all_orbits(test_graph) == 42

# --- Day 6: Universal Orbit Map ---
data = parse_data(data)
graph = make_graph(data)
part1 = count_all_orbits(graph)
print(f"Part 1: {part1}")

# --- Part Two ---

test_data_2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

test_data_2 = parse_data(test_data_2)
test_graph_2 = make_graph(test_data_2)

def get_path(obj, graph, destination = "COM"):
	if obj == destination:
		return [destination]
	parent_path = get_path(graph[obj], graph, destination)
	return parent_path + [obj]

assert get_path("SAN", test_graph_2) == ['COM', 'B', 'C', 'D', 'I', 'SAN']
assert get_path("YOU", test_graph_2) == ['COM', 'B', 'C', 'D', 'E', 'J', 'K', 'YOU']

def find_distance_between_nodes(a, b, graph):
	path_a = get_path(a, graph)
	path_b = get_path(b, graph)
	for idx, item in enumerate(path_a):
		if item != path_b[idx]:
			start_idx = idx
			break
	diff_a = path_a[start_idx:]
	diff_b = path_b[start_idx:]
	return len(diff_a) + len(diff_b) - 2

assert find_distance_between_nodes("YOU", "SAN", test_graph_2) == 4


part2 = find_distance_between_nodes("YOU", "SAN", graph)
print(f"Part 2: {part2}")






