# from day05 import run_code
from itertools import permutations

with open('day07_input.txt') as f:
	insts = [int(val) for val in f.read().split(',')]

# def run_code(inpt_data, initial_input=None):

# --- Day 7: Amplification Circuit ---
def parse_opcode(op):
	op = str(op)
	while len(op) < 5:
		op = '0' + op
	return int(op[-2:]), int(op[2]), int(op[1]), int(op[0])

def multiply(p1, p2, result, data, loc, results):
	# global loc
	data[result] = p1 * p2
	loc += 4
	return loc

def add(p1, p2, result, data, loc, results):
	data[result] = p1 + p2
	loc += 4
	return loc

def inpt(p1, inpts, data, loc, results):
	# print(p1, inpts)
	data[p1] = inpts.pop(0)
	loc += 2
	return loc

def outpt(p1, data, loc, results):
	results.append(p1)
	loc += 2
	return loc

def jump_if_true(p1, result, data, loc, results):
	if p1 != 0:
		loc = result
	else:
		loc += 3
	return loc

def jump_if_false(p1, result, data, loc, results):
	if p1 == 0:
		loc = result
	else:
		loc += 3
	return loc

def less_than(p1, p2, result, data, loc, results):
	data[result] = int(p1 < p2)
	loc += 4
	return loc

def equals(p1, p2, result, data, loc, results):
	data[result] = int(p1 == p2)
	loc += 4
	return loc

def end(*args, **kwargs):
	return

def error(*args, **kwargs):
	print(f"something went wrong, it was called with {args}")

funcs = {
	1: add,
	2: multiply,
	3: inpt,
	4: outpt,
	5: jump_if_true,
	6: jump_if_false,
	7: less_than,
	8: equals,
	99: end,
}

def run_amplifier(inpt_data, initial_input=None):
	# print("==================================================================")
	# print(inpt_data)
	# print("==================================================================")
	data = inpt_data.copy()
	loc = 0
	count = 0
	results = []
	while True and count < 1000: #protect against infinite loop while debugging
		op = data[loc]
		o, p1, p2, p3 = parse_opcode(op)
		# print(f"count: {count} | loc: {loc} | op: {op} | initial_input: {initial_input} | data:{data[loc:loc+4]}")
		f = funcs.get(o, error)
		if o == 4:
			p = data[loc+1]
			params = [p] if p1 == 1 else [data[p]]
		if o == 3:
			params = [data[loc+1], initial_input]
		elif o in (5, 6):
			params = data[loc+1: loc+3]
			params = [param if mode == 1 else data[param] for mode, param in zip((p1, p2), params)]
		elif o in (1, 2, 7, 8):
			params = data[loc+1: loc+4]
			params = [param if mode == 1 else data[param] for mode, param in zip((p1, p2, 1), params)]
		elif o == 99:
			break
		loc = f(*params, data=data, loc=loc, results=results)
		count += 1
	return results[0]

def run_amplifiers(inpt_data, phase_settings):
	data = inpt_data.copy()
	input_signal = 0
	for val in phase_settings:
		input_signal = run_amplifier(data, [val, input_signal])
	return input_signal

from pprint import pprint
# pprint(list(permutations(range(3), r=3)))

def find_max_thruster(inpt_data):
	# max_thrust = -1000000
	# for settings in permutations(range(5), r=5):
	# 	try:
	# 		res = run_amplifiers(inpt_data.copy(), settings)
	# 		if res > max_thrust:
	# 			max_thrust = res
	# 	except:
	# 		pass
	# return max_thrust
	return max(run_amplifiers(inpt_data.copy(), settings) for settings in permutations(range(5), r=5))

class amplifier:
	def parse_opcode(self, op):
		op = str(op)
		while len(op) < 5:
			op = '0' + op
		return int(op[-2:]), int(op[2]), int(op[1]), int(op[0])

	def multiply(self, p1, p2, result):
		# global loc
		self.code[result] = p1 * p2
		self.loc += 4

	def add(self, p1, p2, result):
		self.code[result] = p1 + p2
		self.loc += 4

	def inpt(p1, inpts):
		self.code[p1] = inpts.pop(0)
		loc += 2
		return loc

	def outpt(p1, data, loc, results):
		results.append(p1)
		loc += 2
		return loc

	def jump_if_true(p1, result, data, loc, results):
		if p1 != 0:
			loc = result
		else:
			loc += 3
		return loc

	def jump_if_false(p1, result, data, loc, results):
		if p1 == 0:
			loc = result
		else:
			loc += 3
		return loc

	def less_than(p1, p2, result, data, loc, results):
		data[result] = int(p1 < p2)
		loc += 4
		return loc

	def equals(p1, p2, result, data, loc, results):
		data[result] = int(p1 == p2)
		loc += 4
		return loc

	def end(*args, **kwargs):
		return

	def error(*args, **kwargs):
		print(f"something went wrong, it was called with {args}")

	funcs = {
		1: add,
		2: multiply,
		3: inpt,
		4: outpt,
		5: jump_if_true,
		6: jump_if_false,
		7: less_than,
		8: equals,
		99: end,
	}

	def __init__(self, code, setting):
		self.code = code.copy()
		self.setting = setting
		self.loc = loc
		self.count = 0

	def run_amplifier(input):
		while True and self.count < 1000: #protect against infinite loop while debugging
			op = self.code[self.loc]
			o, p1, p2, p3 = parse_opcode(op)
			# print(f"count: {count} | loc: {loc} | op: {op} | initial_input: {initial_input} | data:{data[loc:loc+4]}")
			f = funcs.get(o, error)
			if o == 4:
				p = self.code[self.loc+1]
				params = [p] if p1 == 1 else [data[p]]
			if o == 3:
				params = [data[loc+1], initial_input]
			elif o in (5, 6):
				params = data[loc+1: loc+3]
				params = [param if mode == 1 else data[param] for mode, param in zip((p1, p2), params)]
			elif o in (1, 2, 7, 8):
				params = data[loc+1: loc+4]
				params = [param if mode == 1 else data[param] for mode, param in zip((p1, p2, 1), params)]
			elif o == 99:
				break
			loc = f(*params, data=data, loc=loc, results=results)
			count += 1
		return results[0]











