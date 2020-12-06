from string import ascii_lowercase

with open("day_06.txt") as f:
	print("Part 1:", sum((len(x) for x in [set().union(*(set(form) for form in group))for group in (group_str.split("\n") for group_str in f.read().split("\n\n"))])))
with open("day_06.txt") as f:
	print("Part 2:", sum((len(x) for x in [set(ascii_lowercase).intersection(*(set(form) for form in group))for group in (group_str.split("\n") for group_str in f.read().split("\n\n"))])))
