from pprint import pprint
from copy import deepcopy

# --- Day 13: Packet Scanners ---

test_input = """0: 3
1: 2
4: 4
6: 4"""

with open('day13_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read()

# -- data structure --
# {
# 	'depth': {
# 		'direction': 1,
# 		'location': 0,
# 		'range': 3
# 	}
# }

def parse_input(puzzle_input):
	layers = puzzle_input.splitlines()
	firewall = {}
	max_depth = 0
	for layer in layers:
		layer = layer.split(': ')
		depth, rng = [int(x) for x in layer]
		firewall[depth] = {
			'direction': 1,
			'location': 0,
			'range': rng
		}
		max_depth = max([depth, max_depth])
	return firewall, max_depth

def move_scanner(scanner):
	next_step = scanner['location'] + scanner['direction']
	if next_step >= scanner['range'] or next_step < 0:
		scanner['direction'] *= -1
	scanner['location'] += scanner['direction']

test_scanner = {'direction': 1, 'location': 0, 'range': 3}
move_scanner(test_scanner)
assert test_scanner['location'] == 1
move_scanner(test_scanner)
assert test_scanner['location'] == 2
move_scanner(test_scanner)
assert test_scanner['location'] == 1
move_scanner(test_scanner)
assert test_scanner['location'] == 0
move_scanner(test_scanner)
assert test_scanner['location'] == 1

def move_scanners(firewall):
	for depth, scanner in firewall.items():
		move_scanner(scanner)

def cross_firewall(firewall, max_depth, short_circuit=False):
	severity = 0
	caught = False
	# move down layers
	for depth in range(max_depth + 1):
		scanner = firewall.get(depth)
		# if there is a scanner on that layer
		if scanner is not None:
			# check if scanner catches you
			if scanner['location'] == 0:
				severity += depth * scanner['range']
				caught = True
		move_scanners(firewall)
	return severity

assert cross_firewall(*parse_input(test_input)) == 24

print "Part 1 solution:", cross_firewall(*parse_input(puzzle_input))

# --- Part Two ---

# The data structure up above is far to slow to test this many times, implementing a solution based on math
def parse_simple(raw_input):
	layers = [layer.split(': ') for layer in raw_input.splitlines()]
	firewall = {int(depth): int(rng) for depth, rng in layers}
	return firewall

def is_caught(delay, depth, rng):
	return (delay + depth) % ((rng - 1) * 2) == 0

def pass_firewall(firewall, delay=0):
	return any(is_caught(delay, depth, rng) for depth, rng in firewall.items())

def find_delay(firewall):
	for delay in range(10000000):
		caught = pass_firewall(firewall, delay)
		if not caught:
			return delay
	return "did not pass"

assert find_delay(parse_simple(test_input)) == 10
print "Part 2 solution:", find_delay(parse_simple(puzzle_input))
