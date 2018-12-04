with open('day16_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read()
commands = puzzle_input.split(',')
print len(commands)


def spin(programs, command):
	assert command[0] == 's'
	raw_distance = int(command[1:])
	dist = raw_distance % len(programs)
	return programs[-dist:] + programs[:-dist]

assert spin([1,2,3,4,5], 's3') == [3, 4, 5, 1, 2]

def exchange(programs, command):
	assert command[0] == 'x'
	idx1, idx2 = (int(x) for x in command[1:].split('/'))
	programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
	return programs

def partner(programs, command):
	assert command[0] == 'p'
	p1, p2 = command[1:].split('/')
	idx1 = programs.index(p1)
	idx2 = programs.index(p2)
	programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
	return programs

permutations = {
	's': spin,
	'x': exchange,
	'p': partner
}

def move(programs, command):
	func = permutations[command[0]]
	return func(programs, command)

def permute_programs(programs, dance_moves):
	permuted = programs
	for dance_move in dance_moves:
		permuted = move(permuted, dance_move)
	return permuted

def dance(progs, moves):
	programs = list(progs)
	programs = permute_programs(programs, moves)
	return ''.join(programs)

test_dance_moves = ['s1', 'x3/4', 'pe/b']
assert dance('abcde', test_dance_moves) == 'baedc'

progs = 'abcdefghijklmnop'
print dance(progs, commands)

def diff_update(programs, diff_indexes):
	return [programs[idx] for idx in diff_indexes]

# print(dif_update(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'], [11, 6, 15, 10, 13, 8, 14, 3, 12, 9, 0, 2, 5, 1, 4, 7]))
# print(['l', 'g', 'p', 'k', 'n', 'i', 'o', 'd', 'm', 'j', 'a', 'c', 'f', 'b', 'e', 'h'])


# assert dif_update(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'], [11, 6, 15, 10, 13, 8, 14, 3, 12, 9, 0, 2, 5, 1, 4, 7]) == ['l', 'g', 'p', 'k', 'n', 'i', 'o', 'd', 'm', 'j', 'a', 'c', 'f', 'b', 'e', 'h']


# def billion_dances(progs, moves):
# 	# for _ in range(1000000000):
# 	original_programs = list(progs)
# 	print 'original programs:', ''.join(original_programs)
# 	diff1 = list(dance(progs, commands))
# 	indexes = [original_programs.index(p) for p in diff1]
# 	programs = list(progs)
# 	# for _ in range(1000000000):
# 	iterations = 0
# 	for count in range(55):
# 		iterations += 1
# 		programs = diff_update(programs, indexes)

# 	return ''.join(programs)
# 	# for _ in range(1000):
# 	# 	programs = permute_programs(programs, moves)
# 	# return programs


def billion_dances(progs, moves):
	# for _ in range(1000000000):
	original = progs
	count = 0
	for _ in range(34):
		count += 1
		progs = dance(progs, moves)
		if progs == original:
			print "cycles:", count
			break

	return progs

print billion_dances(progs, commands)
print ('=====')
print(1000000000 % 42)

