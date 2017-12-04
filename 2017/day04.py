# --- Day 4: High-Entropy Passphrases ---

with open('day04_puzzle_input.txt') as file_input:
	puzzle_input = file_input.read().splitlines()

def valid_passphrase(phrase, sort_letters=False):
	words = phrase.split(' ')
	if sort_letters:
		words = [''.join(sorted(word)) for word in words]
	return len(words) == len(set(words))

def count_phrases(phrases, sort_letters=False):
	valid_phrases = 0
	for phrase in phrases:
		if valid_passphrase(phrase, sort_letters):
			valid_phrases += 1
	return valid_phrases

assert valid_passphrase('aa bb cc dd ee')
assert not valid_passphrase('aa bb cc dd aa')
assert valid_passphrase('aa bb cc dd aaa')

print "Part 1 solution:", count_phrases(puzzle_input)

# --- Part Two ---

assert valid_passphrase('abcde fghij', sort_letters=True)
assert not valid_passphrase('abcde xyz ecdab', sort_letters=True)
assert valid_passphrase('a ab abc abd abf abj', sort_letters=True)
assert valid_passphrase('iiii oiii ooii oooi oooo', sort_letters=True)
assert not valid_passphrase('oiii ioii iioi iiio', sort_letters=True)

print "Part 2 solution:", count_phrases(puzzle_input, sort_letters=True)
