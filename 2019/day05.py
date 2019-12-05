# from day02 import add

with open('day05_input.txt') as f:
	insts = [int(val) for val in f.read().split(',')]

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

def inpt(p1, val, data, loc, results):
	data[p1] = val
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

def run_code(inpt_data, initial_input=None):
	data = inpt_data.copy()
	loc = 0
	count = 0
	results = []
	while True and count < 1000: #protect against infinite loop while debugging
		op = data[loc]
		o, p1, p2, p3 = parse_opcode(op)
		f = funcs.get(o)
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
	return results

# --- Day 5: Sunny with a Chance of Asteroids ---
test1 = run_code([3,9,8,9,10,9,4,9,99,-1,8], 5)
assert test1[-1] == 0
test2 = run_code([3,9,8,9,10,9,4,9,99,-1,8], 8)
assert test2[-1] == 1

test3 = run_code([3,9,7,9,10,9,4,9,99,-1,8], 5)
assert test3[-1] == 1
test4 = run_code([3,9,7,9,10,9,4,9,99,-1,8], 8)
assert test4[-1] == 0

test5 = run_code([3,3,1108,-1,8,3,4,3,99], 5)
assert test5[-1] == 0
test6 = run_code([3,3,1108,-1,8,3,4,3,99], 8)
assert test6[-1] == 1

ops = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
assert run_code(ops, 5)[-1] == 999
assert run_code(ops, 8)[-1] == 1000
assert run_code(ops, 10)[-1] == 1001

part1 = run_code(insts, 1)
print(f"Part 1: {part1[-1]}")

part2 = run_code(insts, 5)
print(f"Part 2: {part2[-1]}")


