from collections import defaultdict
from functools import lru_cache

with open("day_07.txt") as f:
	bag_rules = f.read().splitlines()

def parse_bag_rule(rule):
	name, contents = rule.split(" contain ")
	if contents == "no other bags.":
		contents = []
	else:
		contents = contents.split(", ")
		contents = [(int(bag[0]), simplify(bag[2:])) for bag in contents]
	return simplify(name), contents

def simplify(name):
	return name.rstrip('.s')
rules = [parse_bag_rule(rule) for rule in bag_rules]
bags = defaultdict(list)
for rule in rules:
	for count, color in rule[1]:
		bags[color].append(rule[0])

def get_containing_colors(color):

	return {color}.union(*(get_containing_colors(b) for b in bags[color]))

shiny_containers = get_containing_colors('shiny gold bag')
print("Part 1:", len(shiny_containers) - 1)

bag_contents = dict(rules)
from pprint import pprint

# @lru_cache
def get_total_bags(color):
	return 1 + sum(count * get_total_bags(bag) for count, bag in bag_contents[color])

print("Part 2:", get_total_bags("shiny gold bag") - 1)