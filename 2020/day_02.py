with open("day_02.txt") as f:
	passwords = [line.split(": ") for line in f.read().splitlines()]

def parse_rules(password):
	char = password[0][-1]
	low, high = (int(num) for num in password[0].split()[0].split("-"))
	return low, high, char

def is_valid_password(password):
	low, high, char = parse_rules(password)
	return low <= password[1].count(char) <= high

assert is_valid_password(['1-3 a', 'abcde']) == True
assert is_valid_password(['1-3 b', 'cdefg']) == False
assert is_valid_password(['2-9 c', 'ccccccccc']) == True

# Part 1
print("Part 1")
valid_password_count = len([1 for password in passwords if is_valid_password(password)])
print(valid_password_count)


def is_valid_password_new(password):
	idx1, idx2, char = parse_rules(password)
	idx1 -= 1
	idx2 -= 1
	pw = password[1]
	return (pw[idx1] == char or pw[idx2] == char) and not (pw[idx1] == char and pw[idx2] == char)

assert is_valid_password_new(['1-3 a', 'abcde']) == True
assert is_valid_password_new(['1-3 b', 'cdefg']) == False
assert is_valid_password_new(['2-9 c', 'ccccccccc']) == False

# Part 2
print("Part 2")
valid_password_count = len([1 for password in passwords if is_valid_password_new(password)])
print(valid_password_count)