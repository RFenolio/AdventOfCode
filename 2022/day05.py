import re
import os
import sys

input_file = os.path.join(sys.path[0], "day05_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()

crates = [
    [], #0
    list("WMLF"), #1
    list("BZFMF"), #2
    list("HVRSLQ"), #3
    list("FSVQPMTJ"), #4
    list("LSW"), #5
    list("FVPMRJW"), #6
    list("JQCPNRF"), #7
    list("VHPSZWRB"), #8
    list("BMJCGHZW"), #9
]

example = [
    [],
    list("ZN"),
    list("MCD"),
    ["P"]
]


example_instruction = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()

pattern = re.compile(r"move ([0-9]*) from ([0-9]*) to ([0-9]*)")

def move_crate(stacks, instruction):
    count, start, end = (int(val) for val in pattern.match(instruction).groups(int))
    for _ in range(count):
        if stacks[start]:
            stacks[end].append(stacks[start].pop())



def move_stack(stacks, instruction):
    count, start, end = (int(val) for val in pattern.match(instruction).groups(int))
    if stacks[start]:
        stacks[end].extend(stacks[start][-count:])
        for _ in range(count):
            stacks[start].pop()

for line in puzzle_input:
    move_stack(crates, line)

res = "".join(stack[-1] for stack in crates if stack)
print(res)