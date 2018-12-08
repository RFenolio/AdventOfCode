with open('day08_input.txt') as f:
	puzzle_input = f.read().split(' ')
	puzzle_input = [int(num) for num in puzzle_input]

# print(puzzle_input[:200])

test_input = [int(num) for num in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(' ')]

class Node:
	def __init__(self):
		self.children = []
		self.metadata = []


def parse_input(nums):
	num_children = nums.pop(0)
	num_metadata = nums.pop(0)
	node = Node()
	for _ in range(num_children):
		child, nums = parse_input(nums)
		node.children.append(child)
	node.metadata = nums[:num_metadata]
	nums = nums[num_metadata:]
	return node, nums

test_res, test_nums = parse_input(test_input)
# print(res.children)
# print(res.metadata)
# for node in res.children:
# 	print(node.children)
# 	print(node.metadata)
def check_metadata(tree):
	nodes = [tree]
	meta_total = 0
	while nodes:
		node = nodes.pop()
		nodes.extend(node.children)
		meta_total += sum(node.metadata)
	return meta_total

test_total = check_metadata(test_res)
assert test_total == 138

tree, nums = parse_input(puzzle_input)
check = check_metadata(tree)
print("Part 1:")
print(check)

def root_value(node):
	if not node.children:
		return sum(node.metadata)

	nodes = [node.children[meta-1] for meta in node.metadata if meta <= len(node.children)]
	root_vals = [root_value(node) for node in nodes]
	return sum(root_vals)

# Part 2

print(len(test_res.children), test_res.metadata)
assert root_value(test_res.children[1].children[0]) == 99
assert root_value(test_res.children[1]) == 0
assert root_value(test_res.children[0]) == 33
assert root_value(test_res) == 66

print("Part 2:")
print(root_value(tree))

