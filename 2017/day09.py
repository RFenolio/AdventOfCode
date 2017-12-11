with open('day09_puzzle_input.txt') as puzz:
	puzzle_input = puzz.read()

# --- Day 9: Stream Processing ---

def score_stream(stream):
	garbage = False
	cancel = False
	streams = []
	score = 0
	num_garbage = 0
	for char in stream:
		if cancel:
			# print char, 1
			cancel = False
			continue
		elif char == '!':
			# print char, 7
			cancel = True
			continue
		elif char == '>':
			# print char, 2
			garbage = False
			continue
		elif garbage:
			# print char, 3
			num_garbage += 1
			continue
		elif char == '<':
			# print char, 4
			garbage = True
			continue
		elif char == '{':
			# print char, 5
			streams.append(char)
		elif char == '}':
			# print char, 6
			score += len(streams)
			streams.pop()
	return score, num_garbage


assert score_stream('{}')[0] == 1
assert score_stream('{{{}}}')[0] == 6
assert score_stream('{{},{}}')[0] == 5
assert score_stream('{{{},{},{{}}}}')[0] == 16
assert score_stream('{<a>,<a>,<a>,<a>}')[0] == 1
assert score_stream('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == 9
assert score_stream('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0] == 9
assert score_stream('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0] == 3

puzzle_result = score_stream(puzzle_input)
print "Part 1 solution:", puzzle_result[0]

# --- Part Two --- 
assert score_stream('<>')[1] == 0
assert score_stream('<random characters>')[1] == 17
assert score_stream('<<<<>')[1] == 3
assert score_stream('<{!>}>')[1] == 2
assert score_stream('<!!>')[1] == 0
assert score_stream('<!!!>>')[1] == 0
assert score_stream('<{o"i!a,<{i<a>')[1] == 10

print "Part 2 solution:", puzzle_result[1]







