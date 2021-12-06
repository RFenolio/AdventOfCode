import os
import sys
from typing import List
"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day06_input.txt")
with open(input_file) as f:
    puzzle_input = [int(val) for val in f.read().split(",")]

"""
Part 1
"""
def calculate_fish(fish_ages: List[int], num_days: int):
    # calculate number of fish of each age
    fish_counts: List[int] = [0] * 9
    for fish in fish_ages:
        fish_counts[fish] += 1
    
    # model fish for a number of days
    for _ in range(num_days):
        fish_spawning_today = fish_counts.pop(0)
        fish_counts[6] += fish_spawning_today
        fish_counts.append(fish_spawning_today)
    
    return sum(fish_counts)
    
test_fish = [3,4,3,1,2]
assert calculate_fish(test_fish, 80) == 5934
print("Part 1:", calculate_fish(puzzle_input, 80))


"""
Part 2
"""
assert calculate_fish(test_fish, 256) == 26984457539
print("Part 1:", calculate_fish(puzzle_input, 256))