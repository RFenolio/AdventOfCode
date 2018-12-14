def get_map(filename):
	with open(filename) as f:
		puzzle_input = f.read().splitlines()
	tracks = puzzle_input
	return tracks

# Testing line parsing, delete later
test_tracks = get_map('day13_test_input.txt')
# line0 = test_tracks[0]
# for char in line0:
# 	if char == '\\':
# 		print("it worked")
# 	print(char)
tracks = get_map('day12_input.txt')
cars = 0
for line in tracks:
	for char in line:
		if char in '><^v':
			cars += 1
print(cars)

class Node:
	def __init__(val, x, y, tracks):
		self.val = val
		self.x = x
		self.y = y
		self.options = {}
		
	def _make_options():
		options = {}
		if val == '|':
			

