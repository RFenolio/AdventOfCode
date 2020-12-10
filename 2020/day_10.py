from functools import lru_cache

with open("day_10.txt") as f:
	numbers = sorted([int(num) for num in f.read().splitlines()])

zipped = list(zip(numbers, numbers[1:]))
diffs = [b-a for a, b in zipped]
print("Part 1:", (diffs.count(1)+1) * (diffs.count(3)+1))


@lru_cache
def count_combinations(nums, n):
	total = 0
	if n == 0:
		return 1
	if (n - 1) >= 0 and nums[n] - nums[n-1] <= 3:
		total += count_combinations(nums, n-1)
	if (n - 2) >= 0 and nums[n] - nums[n-2] <= 3:
		total += count_combinations(nums, n-2)
	if (n - 3) >= 0 and nums[n] - nums[n-3] <= 3:
		total += count_combinations(nums, n-3)
	return total

numbers.append(numbers[-1] + 3)
numbers = tuple([0] + numbers)
print("Part 2:", count_combinations(numbers, (len(numbers)-1)))
