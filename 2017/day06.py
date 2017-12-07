

with open('day06_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read().splitlines()

puzzle_input = [4, 10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]

test_banks = [0, 2, 7, 0]

def redistribute(banks, part=1):
	tested_banks = []
	tested_banks.append(tuple(banks))
	count = 0
	while True:
		if count > 10000000:
			break
		idx = banks.index(max(banks))
		max_val = banks[idx]
		banks[idx] = 0
		for offset in range(max_val):
			banks[(idx + 1 + offset) % len(banks)] += 1
		if tuple(banks) in tested_banks:
			tested_banks.append(tuple(banks))
			break
		else:
			tested_banks.append(tuple(banks))
		count += 1

	if part == 1:
		return len(tested_banks) - 1
	if part == 2:
		return len(tested_banks) - tested_banks.index(tuple(banks)) - 1
	else:
		return False

assert redistribute(test_banks, part=1
	) == 5
print "Part 1 solution:", redistribute(puzzle_input)

# --- Part Two ---

assert redistribute(test_banks, part=2) == 4
print "part 2 solution:", redistribute(puzzle_input, part=2)