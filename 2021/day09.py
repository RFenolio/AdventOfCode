import os
import sys
from math import prod
from typing import List, Set, Tuple

"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day09_input.txt")
with open(input_file) as f:
    puzzle = f.read().splitlines()

test_puzzle = """2199943210
3987894921
9856789892
8767896789
9899965678""".split('\n')

def get_surrounding(point: Tuple[int, int], cave_map: List[str]) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    if point[0] > 0:
        res.append((point[0] - 1, point[1]))
    if point[0] < len(cave_map) - 1:
        res.append((point[0] + 1, point[1]))
    if point[1] > 0:
        res.append((point[0], point[1] - 1))
    if point[1] < len(cave_map[0]) - 1:
        res.append((point[0], point[1] + 1))
    return res

def is_low_point(row: int, col: int, cave_map: List[str]) -> bool:
    point_height = cave_map[row][col]
    surrounding = get_surrounding((row, col), cave_map)
    return all(point_height < cave_map[point[0]][point[1]] for point in surrounding)

assert is_low_point(0, 1, test_puzzle) == True
assert is_low_point(2, 2, test_puzzle) == True
assert is_low_point(1, 9, test_puzzle) == False

def find_low_points(cave_map: List[str]) -> List[Tuple[int, int]]:
    points: List[Tuple[int, int]] = []
    for row_idx, row in enumerate(cave_map):
        for col_idx, _ in enumerate(row):
            if is_low_point(row_idx, col_idx, cave_map):
                points.append((row_idx, col_idx))
    return points

def calculate_low_points(cave_map: List[str]) -> int:
    points = find_low_points(cave_map)
    return sum(int(cave_map[point[0]][point[1]]) + 1 for point in points)

assert calculate_low_points(test_puzzle) == 15
print("Part 1:", calculate_low_points(puzzle))

def find_basin(low_point: Tuple[int, int], cave_map: List[str]) -> Set[Tuple[int, int]]:
    points_to_check = [low_point]
    basin_points = set()
    basin_points.add(low_point)
    while points_to_check:
        point = points_to_check.pop()
        surrounding = get_surrounding(point, cave_map)
        for point in surrounding:
            if point not in basin_points and cave_map[point[0]][point[1]] != "9":
                basin_points.add(point)
                points_to_check.append(point)
    return basin_points

def find_basins(cave_map: List[str]) -> List[Set[Tuple[int, int]]]:
    low_points = find_low_points(cave_map)
    basins = [find_basin(point, cave_map) for point in low_points]
    basins.sort(key=len)
    return basins

assert len(find_basin((0,9), test_puzzle)) == 9
test_basins = find_basins(test_puzzle)
assert prod([len(basin) for basin in test_basins[-3:]]) == 1134
puzzle_basins = find_basins(puzzle)
print("Part 2:", prod([len(basin) for basin in puzzle_basins[-3:]]))
