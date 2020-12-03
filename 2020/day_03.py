with open("day_03.txt") as f:
	trees = f.read().splitlines()
WIDTH = len(trees[0])

def count_trees(r, d):
	idx = 0
	tree_count = 0
	row = 0
	while row < len(trees):
		pos = idx % WIDTH
		if trees[row][pos] == '#':
			tree_count += 1
		idx += r
		row += d
	return tree_count

# Part 1
print(count_trees(3,1))

# Part 2
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
product = 1
for slope in slopes:
	product *= count_trees(*slope)
print (product)