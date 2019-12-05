# from day02 import add

with open('day05_input.txt') as f:
	insts = [int(val) for val in f.read().split(',')]

def parse_opcode(op):
	op = str(op)
	while len(op) < 5:
		op = '0' + op
	return int(op[-2:]), int(op[2]), int(op[1]), int(op[0])

def multiply(p1, p2, result, data):
	global loc
	data[result] = p1 * p2
	loc += 4
	return data

def add(p1, p2, result, data):
	global loc
	data[result] = p1 + p2
	loc += 4
	return data

def inpt(p1, data):
	global loc
	global val
	data[p1] = val
	loc += 2
	return data

def outpt(p1, data):
	global loc
	global val
	global results
	val = data[p1]
	results.append(val)
	loc += 2
	return data

def jump_if_true(p1, result, data):
	global loc
	if p1 != 0:
		loc = result
	else:
		loc += 3
	return data

def jump_if_false(p1, result, data):
	global loc
	if p1 == 0:
		loc = result
	else:
		loc += 3
	return data

def less_than(p1, p2, result, data):
	global loc
	data[result] = int(p1 < p2)
	loc += 4
	return data

def equals(p1, p2, result, data):
	global loc
	data[result] = int(p1 == p2)
	loc += 4
	return data

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

loc = 0
count = 0
val = 5
results = []

# def run(data):
while True and count < 1000:
	op = insts[loc]
	o, p1, p2, p3 = parse_opcode(op)
	f = funcs.get(o)
	if o in (3, 4):
		params = insts[loc+1: loc+2]
	elif o in (5, 6):
		params = insts[loc+1: loc+3]
		params = [param if mode == 1 else insts[param] for mode, param in zip((p1, p2), params)]
	elif o in (1, 2, 7, 8):
		params = insts[loc+1: loc+4]
		params = [param if mode == 1 else insts[param] for mode, param in zip((p1, p2, 1), params)]
	elif o == 99:
		break
	f(*params, data=insts)
	count += 1

print("results:", results)



