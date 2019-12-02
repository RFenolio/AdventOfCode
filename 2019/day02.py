with open("day02_input.txt") as f:
	data = f.read()
	data = [int(num) for num in data.split(',')]


def multiply(idx1, idx2, result, data):
	data[result] = data[idx1] * data[idx2]
	return data

def add(idx1, idx2, result, data):
	data[result] = data[idx1] + data[idx2]
	return data

def process_instructions(data):
	for idx in range(0, len(data), 4):
		ops = data[idx:idx+4]
		if len(ops) == 4:
			op, idx1, idx2, result = ops
		else:
			op = ops[0]
		if op == 1:
			fn = add
		elif op == 2:
			fn = multiply
		elif op == 99:
			break
		else:
			raise('that is not a valid command')
		data = fn(idx1, idx2, result, data)
	return data

res1 = process_instructions([1,0,0,0,99])
assert res1 == [2,0,0,0,99]
res2 = process_instructions([2,3,0,3,99])
assert res2 == [2,3,0,6,99]
res3 = process_instructions([2,4,4,5,99,0])
assert res3 == [2,4,4,5,99,9801]
res4 = process_instructions([1,1,1,4,99,5,6,0,99])
assert res4 == [30,1,1,4,2,5,6,0,99]
res5 = process_instructions([1,9,10,3,2,3,11,0,99,30,40,50])
assert res5 == [3500,9,10,70,2,3,11,0,99,30,40,50]

# --- Day 2: 1202 Program Alarm ---
day2_data = data.copy()
day2_data[1] = 12
day2_data[2] = 2
res = process_instructions(day2_data)
print("Part 1:", res[0])

# --- Part Two ---
for x in range(100):
	for y in range(100):
		part2_input = data.copy()
		part2_input[1] = x
		part2_input[2] = y
		res = process_instructions(part2_input)
		if res[0] == 19690720:
			print("Part 2:", (x * 100) + y)
			break
