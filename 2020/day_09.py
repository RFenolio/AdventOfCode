with open("day_09.txt") as f:
	numbers = [int(num) for num in f.read().splitlines()]

def check_validity(list):
	previous_nums = list[:-1]
	target = list[-1]
	checked = set()
	for num in previous_nums:
		if target - num in checked:
			return True
		else:
			checked.add(num)
	return False

def find_invalid(input, size=25):
	size += 1
	for idx in range(len(input) - size):
		section = input[idx: idx + size]
		if not check_validity(section):
			return(section[-1])

# part 2
bad_num = find_invalid(numbers)
print(f"Part 1: {bad_num}")

# part 2
bad_idx = numbers.index(bad_num)

start = 0
for i in range(1, bad_idx+1):
	while(sum(numbers[start: i]) > bad_num):
		start += 1
	if sum(numbers[start:i]) == bad_num:
		low = min(numbers[start:i])
		high = max(numbers[start:i])
		print(low, high)
		print(sum((low, high)))