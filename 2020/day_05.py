
with open("day_05.txt") as f:
	seats = f.read().splitlines()

def get_seat_id(seat_code: str) -> int:
	"""It's just a binary string"""
	return int(seat_code.translate(str.maketrans('FBLR', '0101')), base=2)

assert get_seat_id("BFFFBBFRRR") == 567
assert get_seat_id("FFFBBBFRRR") == 119
assert get_seat_id("BBFFBBFRLL") == 820

# Part 1
seat_ids = set(get_seat_id(seat) for seat in seats)
print("Part 1:", max(seat_ids))

# Part 2
your_seat = [seat for seat in range(948) if (seat not in seat_ids and seat+1 in seat_ids and seat-1 in seat_ids)][0]
print("Part 2:", your_seat)