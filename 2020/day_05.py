
with open("day_05.txt") as f:
	seats = f.read().splitlines()

def calculate_row(row_code: str) -> int:
	seat = list(range(128))
	for char in row_code:
		mid = len(seat)//2
		if char == "F":
			seat = seat[:mid]
		else: # char == "B"
			seat = seat[mid:]
	return seat[0]

assert calculate_row("FBFBBFF") == 44

def calculate_col(col_code: str) -> int:
	col = list(range(8))
	for char in col_code:
		mid = len(col)//2
		if char == "L":
			col = col[:mid]
		else: # char == "B"
			col = col[mid:]
	return col[0]

assert calculate_col("RLR") == 5

def get_seat_id(seat_code: str) -> int:
	row_code = seat_code[:7]
	col_code = seat_code[7:]
	return (calculate_row(row_code) * 8) +calculate_col(col_code)


assert get_seat_id("BFFFBBFRRR") == 567
assert get_seat_id("FFFBBBFRRR") == 119
assert get_seat_id("BBFFBBFRLL") == 820

# Part 1
seat_ids = set(get_seat_id(seat) for seat in seats)
print("Part 1:", max(seat_ids))

# Part 2
your_seat = [seat for seat in range(948) if (seat not in seat_ids and seat+1 in seat_ids and seat-1 in seat_ids)][0]
print("Part 2:", your_seat)