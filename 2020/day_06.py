from string import ascii_lowercase

with open("day_06.txt") as f:
	groups = [group_str.split("\n") for group_str in f.read().split("\n\n")]

print("Part 1:", sum((len(x) for x in [set().union(*(set(form) for form in group))for group in groups])))

print("Part 2:", sum((len(x) for x in [set(ascii_lowercase).intersection(*(set(form) for form in group))for group in groups])))
