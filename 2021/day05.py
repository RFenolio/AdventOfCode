import os
import sys

"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day05_input.txt")
with open(input_file) as f:
    puzzle_input = f.read().splitlines()
    puzzle_input = [[[int(val) for val in part.split(",")] for part in line.split(" -> ")] for line in puzzle_input]
    
test_input_file = os.path.join(sys.path[0], "day05_test_input.txt")
with open(test_input_file) as f:
    puzzle_test_input = f.read().splitlines()
    puzzle_test_input = [[[int(val) for val in part.split(",")] for part in line.split(" -> ")] for line in puzzle_test_input]

def make_grid(size):
    return [[0] * size for _ in range(size)]

def add_line(grid, line):
    start, end = line
    dx = get_direction(start[0], end[0])
    dy = get_direction(start[1], end[1])
    x = start[0]
    y = start[1]
    while (x != end[0] or y != end[1]):
        grid[y][x] += 1
        x += dx
        y += dy
    grid[end[1]][end[0]] += 1

def get_direction(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    elif a == b:
        return 0 

def count_hotspots(grid):
    return sum(sum(i > 1 for i in row) for row in grid)

def find_hotspots(size, input, diagonal=False):
    grid = make_grid(size)
    for line in input:
        if not diagonal:
            if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
                add_line(grid, line)
        else:
            add_line(grid, line)
    return count_hotspots(grid)

assert find_hotspots(10, puzzle_test_input) == 5
print("Part 1:", find_hotspots(1000, puzzle_input))

assert find_hotspots(10, puzzle_test_input, diagonal=True) == 12
print("Part 2:", find_hotspots(1000, puzzle_input, diagonal=True))
