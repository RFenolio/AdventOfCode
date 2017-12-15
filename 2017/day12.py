# --- Day 12: Digital Plumber ---

test_graph = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''

with open('day12_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read()

def parse_graph(graph):
	nodes = [node.split(' ') for node in graph.splitlines()]
	nodes = {node[0]: [item.strip(',') for item in node[2:]] for node in nodes}
	return nodes

def find_cluster_size(graph, starting_node, visited=None):
	if visited is None:
		visited = set()
	to_visit = [starting_node]
	max_loop = 100000
	count = 0
	while to_visit and count < max_loop:
		count += 1
		current_node = to_visit.pop()
		if current_node not in visited:
			visited.add(current_node)
			to_visit.extend(graph[current_node])
	return len(visited), visited

test_graph = parse_graph(test_graph)
assert find_cluster_size(test_graph, '0')[0] == 6

puzzle_graph = parse_graph(puzzle_input)

print "Part 1 solution:", find_cluster_size(puzzle_graph, '0')[0]

def count_groups(graph):
	visited = set()
	groups = 0
	for node in graph:
		if node not in visited:
			groups += 1
			visited = find_cluster_size(graph, node, visited)[1]
	return groups

assert count_groups(test_graph) == 2
print "Part 2 solution:", count_groups(puzzle_graph)
