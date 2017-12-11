
# --- Day 10: Knot Hash ---

puzzle_input = '63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24'
part1_input = [int(val) for val in puzzle_input.split(',')]
test_input = [3, 4, 1, 5]

def hash_function(list_length, operations):
	zero_idx = 0
	skip_size = 0
	knot = range(list_length)
	for op in operations:
		# reverse a section
		knot[:op] = knot[:op][::-1]
		# find new list position
		new_start = (op + skip_size) % list_length
		# update zero_idx
		zero_idx = (zero_idx + (list_length - new_start)) % list_length
		# make new list
		knot = knot[new_start:] + knot[:new_start]
		# update skip_size
		skip_size += 1

	return knot[zero_idx:] + knot[:zero_idx]

assert hash_function(5, test_input) == [3, 4, 2, 1, 0]
# print hash_function(5, test_input)
# testing = range(5)
# print testing
# a = 3
# testing[:a] = testing[:a][::-1]
# print testing
# testing = testing[a:] + testing[:a]
# print testing

part_1_list = hash_function(256, part1_input)
print "Part 1 solution:"
print part_1_list[:2]
print part_1_list[0] * part_1_list[1]



# --- Part Two ---
def hash_round(knot, operations, zero_idx, skip_size):
	list_length = len(knot)
	for op in operations:
		# reverse a section
		knot[:op] = knot[:op][::-1]
		# find new list position
		new_start = (op + skip_size) % list_length
		# update zero_idx
		zero_idx = (zero_idx + (list_length - new_start)) % list_length
		# make new list
		knot = knot[new_start:] + knot[:new_start]
		# update skip_size
		skip_size += 1

	return knot, zero_idx, skip_size

def make_operations(puzzle_input):
	return [ord(char) for char in puzzle_input] + [17, 31, 73, 47, 23]

assert make_operations('1,2,3') == [49,44,50,44,51,17,31,73,47,23]

def bitwise_combine(nums):
	assert len(nums) == 16
	return reduce(lambda x, y: x ^ y, nums)

test_nums = [65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]
assert bitwise_combine(test_nums) == 64

def hash_rounds(puzzle_input):
	ops = make_operations(puzzle_input)
	knot = range(256)
	zero_idx = 0
	skip_size = 0
	for _ in range(64):
		knot, zero_idx, skip_size = hash_round(knot, ops, zero_idx, skip_size)
	# reset original zero idx
	knot = knot[zero_idx:] + knot[:zero_idx]
	chunks = [knot[idx:idx + 16] for idx in range(0, 256, 16)]
	dense = [bitwise_combine(chunk) for chunk in chunks]
	hex_vals = ["{:02x}".format(chunk) for chunk in dense]
	return "".join(hex_vals) 

assert hash_rounds('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert hash_rounds('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert hash_rounds('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert hash_rounds('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

print "Part 2 solution:", hash_rounds(puzzle_input)











