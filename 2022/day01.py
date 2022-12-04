import os
import sys

input_file = os.path.join(sys.path[0], "day01_input.txt")
with open(input_file) as f:
	puzzle_input = f.read()

sample_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
print(sample_input)

#  Part 1
def count_calories(input):
    return [sum([int(x) for x in elf.split("\n")]) for elf in input.split("\n\n")]

test_calories = count_calories(sample_input)
# print(test)
assert(test_calories == [6000, 4000, 11000, 24000, 10000])

calories = count_calories(puzzle_input)
print("Part 1: ", max(count_calories(puzzle_input)))

# part 2
print("Part 2: ", sum(sorted(calories)[-3:]))