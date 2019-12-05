start = 246515
end =739105

# --- Day 4: Secure Container ---

def has_double(pwd):
	return any(pwd[x] == pwd[x-1] for x in range(1, len(pwd)))

assert has_double('abbcd') == True
assert has_double('abcde') == False

def is_ascending(pwd):
	return list(pwd) == sorted(pwd)

assert is_ascending('123456') == True
assert is_ascending('123654') == False

def is_valid_password(num):
	pwd = str(num)
	return (
		len(pwd) == 6
		and is_ascending(pwd)
		and has_double(pwd)
	)

assert is_valid_password(111111) == True
assert is_valid_password(223450) == False
assert is_valid_password(123789) == False

# --- Part Two ---
from itertools import groupby
def no_overlapping_groups(pwd):
	count_dups = [sum(1 for _ in group) for _, group in groupby(pwd)]
	return 2 in count_dups
assert no_overlapping_groups('112233') == True
assert no_overlapping_groups('123444') == False
assert no_overlapping_groups('111122') == True



count = 0
part_2_count = 0
for val in range(start, end + 1):
	if is_valid_password(val):
		count += 1
		if no_overlapping_groups(str(val)):
			part_2_count += 1
print(count)
def is_valid_password_2(num):
	pwd = str(num)
	return (
		len(pwd) == 6
		and is_ascending(pwd)
		and has_double(pwd)
		and no_overlapping_groups(pwd)
	)
part_2_count = 0

for val in range(start, end + 1):
	if is_valid_password_2(val):
		part_2_count += 1

print(part_2_count)