
from itertools import chain

with open("day03_input.txt") as f:
	puzzzle_input = f.read().splitlines()

def make_fabric(x, y):
	return [[0 for x in range(x)] for y in range(y)]
fabric = [[0 for x in range(1000)] for y in range(1000)]
assert fabric == make_fabric(1000, 1000)
assert make_fabric(11, 9) == [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
]

class Claim:
	"""
	takes a claim such as '#1 @ 338,764: 20x24'
	and splits it into it's component parts with names
	"""
	def __init__(self, claim):
		'#1 @ 338,764: 20x24'
		parts = claim.split(' ')
		self.id = parts[0]
		left, top = parts[2].strip(':').split(',')
		self.left = int(left)
		self.top = int(top)
		width, height = parts[3].split('x')
		self.width = int(width)
		self.height = int(height)

test_claim = Claim('#1 @ 338,764: 20x24')
assert test_claim.id == '#1'
assert test_claim.left == 338
assert test_claim.top == 764
assert test_claim.width == 20
assert test_claim.height == 24

def update_fabric(fabric, claim):
	for x in range(claim.height):
		for y in range(claim.width):
			fabric[x + claim.top][y + claim.left] += 1
	return fabric


assert update_fabric(make_fabric(11, 9), Claim('#123 @ 3,2: 5x4')) == [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
]

claims = [Claim(item) for item in puzzzle_input]
def check_overlap(claims, x=1000, y=1000):
	fabric = make_fabric(x, y)
	for claim in claims:
		fabric = update_fabric(fabric, claim)
	overlaps = 0
	for val in chain(*fabric):
		if val > 1:
			overlaps += 1
	return overlaps, fabric

test_claims = [Claim(item) for item in ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']]
assert check_overlap(test_claims)[0] == 4

part1, f1 = check_overlap(claims)
print(part1)

# Part 2
def check_clear(fabric, claim):
	for x in range(claim.height):
		for y in range(claim.width):
			if fabric[x + claim.top][y + claim.left] != 1:
				return False
	return True
test2 = make_fabric(11, 9)
for claim in test_claims:
	test2 = update_fabric(test2, claim)
from pprint import pprint
assert check_clear(test2, test_claims[0]) == False
assert check_clear(test2, test_claims[2]) == True

for claim in claims:
	if check_clear(f1, claim):
		print(claim.id)

