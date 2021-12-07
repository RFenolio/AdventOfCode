import os
import sys


"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day07_input.txt")
with open(input_file) as f:
    puzzle_input = [int(val) for val in f.read().split(",")]

test_input = [16,1,2,0,4,2,7,1,2,14]

def find_straight_fuel(crabs, position):
    return sum(abs(x - position) for x in crabs)

def crab_sum(dist):
    return (dist * (dist + 1)) // 2

def find_crab_dist_fuel(crabs, position):
    return sum(crab_sum(abs(x - position)) for x in crabs)

def find_fuel(func, crabs):
    return min(func(crabs, position) for position in range(min(crabs), max(crabs)+1))

assert find_fuel(find_straight_fuel, test_input) == 37
print("Part 1:", find_fuel(find_straight_fuel, puzzle_input))

assert find_fuel(find_crab_dist_fuel, test_input) == 168
print("Part 2:", find_fuel(find_crab_dist_fuel, puzzle_input))