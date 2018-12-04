from datetime import datetime
from pprint import pprint

with open('day04_input.txt') as f:
	puzzle_input = f.read().splitlines()
puzzle_input.sort()

def get_time(item):
	iso = item[1:17]
	return datetime.fromisoformat(iso)

def split_guards(input):
	res = {}
	current = None
	for item in input:
		parsed = item.split(' ')
		if parsed[2] == 'Guard':
			current = parsed[3]
		else:
			l = res.get(current, [])
			l.append(item)
			res[current] = l
	return res

with open('day04_test_input.txt') as tf:
	test_input = tf.read().splitlines()
test_res = split_guards(test_input)
pprint(test_res)

def sleeping_guard(guard):
	pairs = zip(guard[::2], guard[1::2])
	sleeping = [0]*60
	for start, end in pairs:
		s = get_time(start)
		e = get_time(end)
		for idx in range(s.minute, e.minute):
			sleeping[idx] += 1
	return sleeping

def sleeping_guards(guards):
	return {guard: sleeping_guard(times) for guard, times in guards.items()}

def part1(puzzle_input):
	inpt = split_guards(puzzle_input)
	sleeping = sleeping_guards(inpt)
	most_sleep = 0
	guard_id = None
	minute = None
	for guard, hist in sleeping.items():
		total_time = sum(hist)
		if total_time > most_sleep:
			guard_id = guard
			most_sleep = total_time
			minute = hist.index(max(hist))
	return int(guard_id[1:]) * minute

assert part1(test_input) == 240
part1_solution = part1(puzzle_input)
print(f'Part 1 Solution: {part1_solution}')

def part2(puzzle_input):
	inpt = split_guards(puzzle_input)
	sleeping = sleeping_guards(inpt)
	most_sleep = 0
	guard_id = None
	minute = None
	for guard, hist in sleeping.items():
		max_min = max(hist)
		if max_min > most_sleep:
			guard_id = guard
			most_sleep = max(hist)
			minute = hist.index(max(hist))
	return int(guard_id[1:]) * minute

assert part2(test_input) == 4455
part2_solution = part2(puzzle_input)
print(f'Part 2 Solution: {part2_solution}')