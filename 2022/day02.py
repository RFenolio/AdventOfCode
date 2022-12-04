import os
import sys

input_file = os.path.join(sys.path[0], "day02_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()

test_input = """A Y
B X
C Z""".splitlines()
print(test_input)

scores = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3 ,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3
}
assert((sum(scores[game] for game in test_input)) == 15)
print("Part 1:", sum(scores[game] for game in puzzle_input))

scores_2 = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3 ,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1
}
assert((sum(scores_2[game] for game in test_input)) == 12)
print("Part 2:", sum(scores_2[game] for game in puzzle_input))