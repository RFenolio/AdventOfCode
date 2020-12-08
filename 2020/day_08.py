with open("day_08.txt") as f:
	instructions = f.read().splitlines()

def parse_instruction(line):
	inst, num = line.split()
	return (inst, int(num))

test_instructions = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split('\n')
test_instructions = [parse_instruction(line) for line in test_instructions]
instructions = [parse_instruction(line) for line in instructions]

def run_code(inst, change=None):
	instructions = inst[:]
	idx = 0
	acc = 0
	called = set()
	if change is not None and instructions[change][0] in ("jmp", "nop"):
		if instructions[change][0] == "jmp":
			instructions[change] = ("nop", instructions[change][1])
		else:
			instructions[change] = ("jmp", instructions[change][1])
	while 0 <= idx < len(instructions):
		if idx in called:
			break
		else:
			called.add(idx)
		command, value = instructions[idx]
		if command == "acc":
			acc += value
			idx += 1
		elif command == "jmp":
			idx += value
		else: # no op
			idx += 1
	return acc,  idx == len(instructions)

assert run_code(test_instructions) == (5, False)
print('Part 1:', run_code(instructions))

# Part 2
def find_bad_instruction(instructions):
	for num in range(len(instructions)):
		res, success = run_code(instructions, num)
		if success:
			return num, res

assert find_bad_instruction(test_instructions) == (7, 8)
line, total = find_bad_instruction(instructions)
print(f"Part 2: {total}")


