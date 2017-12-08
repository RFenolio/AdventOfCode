# --- Day 8: I Heard You Like Registers ---

with open('day08_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read()

test_input = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

def parse_puzzle(puzzle):
	puzzle = puzzle.splitlines()
	puzzle = [line.split(' ') for line in puzzle]
	return puzzle

def check_conditional(register, comparator, val):
	if comparator == '<':
		return register < val
	elif comparator == '>':
		return register > val
	elif comparator == '<=':
		return register <= val
	elif comparator == '>=':
		return register >= val
	elif comparator == '==':
		return register == val
	elif comparator == '!=':
		return register != val
	else:
		raise Exception("haven't accounted for that comparator")

def run_single_instruction(line, registers):
	register = line[0]
	register2 = line[4]
	comparator = line[5]
	if register not in registers:
		registers[register] = 0
	if register2 not in registers:
		registers[register2] = 0
	if check_conditional(registers[register2], comparator, int(line[6])):
		if line[1] == 'inc':
			registers[register] += int(line[2])
		elif line[1] == 'dec':
			registers[register] -= int(line[2])
		else:
			raise Exception("that's not a valid command")

def follow_instructions(puzzle):
	puzzle = parse_puzzle(puzzle)
	registers = {}
	max_val = 0
	for line in puzzle:
		run_single_instruction(line, registers)
		local_max = max(registers.values())
		max_val = max(max_val, local_max)
	return max(registers.values()), max_val

assert follow_instructions(test_input) == (1, 10)

print "Part 1 solution:", follow_instructions(puzzle_input)[0]

# --- Part Two ---

print "Part 2 solution:", follow_instructions(puzzle_input)[1]