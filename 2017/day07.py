# --- Day 7: Recursive Circus ---
with open('day07_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read()

test_data = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

def parse_input(puzz):
	lines = puzz.splitlines()
	programs = {}
	for line in lines:
		parse_line(line, programs)
	return programs

def parse_line(line, programs):
	program = line.split(' ')
	programs[program[0]] = program[1:]

def find_bottom(programs):
	progs = set(programs.keys())
	for prog, vals in programs.items():
		if len(vals) > 1:
			pointers = [item.strip(',') for item in vals[2:]]
			for pointer in pointers:
				progs.discard(pointer)
	print progs

test_programs = parse_input(test_data)
find_bottom(test_programs)

programs = parse_input(puzzle_input)
find_bottom(programs)


# -- Part Two ---

def find_weights(bottom, programs):
	vals = programs[bottom]
	bottom_weight = int(vals[0].strip('(').strip(')'))
	total_weight = bottom_weight
	child_weights = []
	if len(vals) > 1:
		children = [item.strip(',') for item in vals[2:]]
		child_weights = [(child, find_weights(child, programs)) for child in children]
		if len(set([child[1] for child in child_weights])) > 1:
			print bottom, bottom_weight, child_weights
	return bottom_weight + sum(child[1] for child in child_weights)


	

find_weights('vtzay', programs)