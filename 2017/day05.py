# --- Day 5: A Maze of Twisty Trampolines, All Alike ---



def run_maze(maze):
	loc = 0
	steps = 0
	while 0 <= loc < len(maze):
		dist = maze[loc]
		maze[loc] += 1
		steps += 1
		loc += dist
	return steps

test_input = """0
3
0
1
-3"""
test_maze = [int(val) for val in test_input.splitlines()]
assert run_maze(test_maze) == 5

with open('day05_puzzle_input.txt') as puzzle:
	maze = [int(val) for val in puzzle.read().splitlines()]

print "Part 1 solution:", run_maze(maze)

# --- Part Two ---

def run_maze_strange_offsets(maze):
	loc = 0
	steps = 0
	while 0 <= loc < len(maze):
		dist = maze[loc]
		if dist >= 3:
			maze[loc] -= 1
		else:
			maze[loc] += 1
		steps += 1
		loc += dist
	return steps
	
test_maze_2 = [int(val) for val in test_input.splitlines()]
assert run_maze_strange_offsets(test_maze_2) == 10
with open('day05_puzzle_input.txt') as puzzle:
	maze2 = [int(val) for val in puzzle.read().splitlines()]
print "Part 2 solution:", run_maze_strange_offsets(maze2)