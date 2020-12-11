from copy import deepcopy
from itertools import chain
from pprint import pprint

with open("day_11.txt") as f:
	seats = [list(line) for line in f.read().splitlines()]

test = [list(line) for line in '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.splitlines()]

test2 = [list(line) for line in '''.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....'''.splitlines()]


DIRECTIONS = [(-1,0),(-1,+1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def get_immediate_seat(row, col, direction, seats):
	row_diff, col_diff = direction
	row += row_diff
	col += col_diff
	return int(0 <= row < len(seats) and 0 <= col < len(seats[0]) and seats[row][col] == "#")

def can_see_seat(row, col, direction, seats):
	row_diff, col_diff = direction
	row += row_diff
	col += col_diff
	ct = 0
	while 0 <= row < len(seats) and 0 <= col < len(seats[0]) and ct < 10000:
		if seats[row][col] == "#":
			return 1
		if seats[row][col] == "L":
			return 0
		row += row_diff
		col += col_diff
	return 0

def count_surrounding_seats(row, col, layout, near_func=get_immediate_seat):
	near_seats = [near_func(row, col, direction, layout) for direction in DIRECTIONS]
	return sum(near_seats)

assert count_surrounding_seats(4, 3, test2, can_see_seat) == 8

# def get_immediate_seat(row, col, direction, seats):
# 	row_diff, col_diff = direction
# 	row += row_diff
# 	col += col_diff
# 	return int(0 <= row < len(seats) and 0 <= col < len(seats[0]) and seats[row][col] == "#")

def update_seats(layout, near_func=get_immediate_seat, threshold=4):
	prev = deepcopy(layout)
	changes = 0
	for row_idx, row in enumerate(prev):
		for col_idx, seat in enumerate(row):
			surrounding = count_surrounding_seats(row_idx, col_idx, prev, near_func)
			if seat == "L" and surrounding == 0:
				layout[row_idx][col_idx] = "#"
				changes += 1
			if seat == "#" and surrounding >= threshold:
				layout[row_idx][col_idx] = "L"
				changes += 1
	return layout, changes

def find_stable(layout, near_func=get_immediate_seat, threshold=4):
	changes = 1
	counter = 0
	while counter < 10000 and changes > 0:
		counter += 1
		layout, changes = update_seats(layout, near_func, threshold)
		# pprint(layout)
	return(count_occupied(layout), changes)

def count_occupied(seats):
	return sum(row.count("#") for row in seats)


# Part 1
# num, changes = find_stable(seats)
# print(num, changes)


# Part 2

test_num2, test_changes2 = find_stable(test, can_see_seat, 5)
print(test_num2, test_changes2)
assert test_num2 == 26
num2, changes2 = find_stable(seats, can_see_seat, 5)
print(num2, changes2)