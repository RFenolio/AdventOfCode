with open('day05_input.txt') as f:
	puzzle_input = f.read()

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"


# def destroy(input):
# 	for idx, char in enumerate(input):
# 		if idx + 1 < len(input):
# 			char2 = input[idx+1]
# 			if ((char.isupper() and char2.islower() and char == char2.upper())
# 				or (char.islower() and char2.isupper() and char.upper() == char2)):
# 				n = input.replace(char + char2, "")
# 				return destroy(n)
# 	return input

test = 'dabAcCaCBAcCcaDA'
# print(destroy(test))
# print(len(destroy(puzzle_input)))

def remove_one(input):
	original = input
	for idx, char in enumerate(input):
			if idx + 1 < len(input):
				char2 = input[idx+1]
				if ((char.isupper() and char2.islower() and char == char2.upper())
					or (char.islower() and char2.isupper() and char.upper() == char2)):
					n = input.replace(char + char2, "")
					return True, n
	return False, original

def destroy(input):
	removed = True
	inpt = input
	while removed:
		removed, inpt = remove_one(inpt)
	return inpt
	
test = 'dabAcCaCBAcCcaDA'
test_res = destroy(test)
print(test_res)
print(len(test_res))

print(len(puzzle_input))
shortest = 50000
for char in UPPER:
	one = puzzle_input.replace(char,'')
	two = one.replace(char.lower(), '')
	print('======================')
	print(len(two))
	res = destroy(two)
	print(char, len(res))
	shortest = min(len(res), shortest)
print(shortest)
