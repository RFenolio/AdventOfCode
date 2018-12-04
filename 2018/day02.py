from collections import Counter
from typing import List, Dict

with open('day02_input.txt') as f:
	puzzle_input = f.read().splitlines()

# print(puzzle_input)

# Part 1
def counter(id: str) -> Dict[str, int]:
	# chars = {}
	# for char in id:
	# 	chars[char] = chars.get(char, 0) + 1
	# return chars
	return Counter(id)

def checksum(ids: List[str]) -> int:
	two = 0
	three = 0
	for id in ids:
		chars = counter(id)
		counts = chars.values()
		if 2 in counts:
			two += 1
		if 3 in counts:
			three += 1
	# print(two, three)
	return two * three

part1 = checksum(puzzle_input)
print(part1)

# Part 2
def find_boxes(puzzle_input: List[str]):
	for a in puzzle_input:
		for b in puzzle_input:
			if compare_ids(a, b) == 1:
				return a, b


def compare_ids(a: str, b: str) -> int:
	difs = 0
	for c, d in zip(a, b):
		if c != d:
			difs += 1
	return difs
assert compare_ids('abcde', 'axcye') == 2
assert compare_ids('fghij', 'fguij') == 1

part2 = find_boxes(puzzle_input)
res = ''
for a, b in zip(*part2):
	if a == b:
		res += a
print(res)
