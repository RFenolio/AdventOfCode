with open('day07_input.txt') as f:
	puzzle_input = f.read().splitlines()

# requirements = {}

def parse_dependency(line, graph, reverse):
	"""
	line example 'Step D must be finished before step L can begin.'

	"""
	parts = line.split(' ')
	node = parts[7]
	dependency = parts[1]
	if node not in graph:
		graph[node] = set()
	if dependency not in graph:
		graph[dependency] = set()
	if node not in reverse:
		reverse[node] = set()
	if dependency not in reverse:
		reverse[dependency] = set()
	graph[node].add(dependency)
	reverse[dependency].add(node)
	return graph, reverse

test_graph, test_reverse = parse_dependency('Step D must be finished before step L can begin.', {}, {})
assert test_graph == {'L': {'D'}, 'D': set()}

def parse_dependencies(lines, graph=None, reverse=None):
	if graph is None:
		graph = {}
	if reverse is None:
		reverse = {}
	for line in lines:
		graph, reverse = parse_dependency(line, graph, reverse)
	return graph, reverse

test_dependencies = [
	"Step C must be finished before step A can begin.",
	"Step C must be finished before step F can begin.",
	"Step A must be finished before step B can begin.",
	"Step A must be finished before step D can begin.",
	"Step B must be finished before step E can begin.",
	"Step D must be finished before step E can begin.",
	"Step F must be finished before step E can begin.",
]
test_graph, test_reverse = parse_dependencies(test_dependencies)
# assert test_graph == {'A': ['C'], 'C': [], 'F': ['C'], 'B': ['A'], 'D': ['A'], 'E': ['B', 'D', 'F']}
# print(test_reverse)

def topo_sort(inpt):
	"""
	takes in a set of instructions, and returns a sorted list of nodes in dependency order
	"""
	graph, reverse = parse_dependencies(inpt)
	res_size = len(graph)
	res = []
	while len(res) < res_size:
		empties = find_empties(graph)
		empties.sort()
		node = empties[0]
		res.append(node)
		remove_node(node, graph)
	return res

def find_empties(graph):
	empties = [key for key, val in graph.items() if not val]
	return empties
assert find_empties(test_graph) == ["C"]

def remove_node(node, graph):
	assert not graph[node]
	graph.pop(node)
	for dependencies in graph.values():
		dependencies.discard(node)

test_sorted = topo_sort(test_dependencies)
print(test_sorted)
part1_list = topo_sort(puzzle_input)
print(''.join(part1_list))
print(len(part1_list))

# print("reverse empties", find_empty(test_reverse))
# a = [3,2,1]
# print(sorted(a))
# print(a)
# def part1():
# 	graph, reverse = parse_dependencies(test)








