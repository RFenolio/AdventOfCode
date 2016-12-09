# PART 1
def supportsTLS(ip_string):
	hypernet_area = True
	valid_ip = False
	for idx, char in enumerate(ip_string):
		if char == '[':
			hypernet_area = False
		elif char == ']':
			hypernet_area = True
		else:
			test = ip_string[idx:idx+4]
			if not hypernet_area and validSequence(test):
				return False
			if hypernet_area and validSequence(test):
				valid_ip = True
	return valid_ip


def validSequence(section):
	if len(section) != 4:
		return False
	good_chars = '[' not in section and ']' not in section
	abba = section[0] == section[3] and section[1] == section[2] and section[0] != section[1]
	return good_chars and abba

assert validSequence('abba')
assert validSequence('oxxo')
assert not validSequence('abcd')
assert not validSequence('abca')
assert not validSequence('abbd')
assert not validSequence('aaaa')
assert supportsTLS('abba[mnop]qrst')
assert not supportsTLS('abcd[bddb]xyyx')
assert not supportsTLS('xyyx[bddb]abcd')
assert not supportsTLS('aaaa[qwer]tyui')
assert supportsTLS('ioxxoj[asdfgh]zxcvbn')

count1 = 0
filename = 'day07.txt'
with open(filename) as f:
	for line in f:
		if supportsTLS(line.strip('\n')):
			count1 += 1

print "Ip addresses in Part 1 that support TLS:", count1


# Part 2
def supportsSSL(ip_string):
	hypernet_area = False
	valid_ip = False
	abas = set()
	# first generate all abas outside of a hypernet area and add them to a set
	for idx, char in enumerate(ip_string):
		if char == '[':
			hypernet_area = True
		elif char == ']':
			hypernet_area = False
		else:
			test = ip_string[idx:idx+3]
			if not hypernet_area and abasequence(test):
				abas.add(test)
	# then look for babs in hypernet areas and check if there is a corresponding aba outside
	hypernet_area = False
	for idx, char in enumerate(ip_string):
		if char == '[':
			hypernet_area = True
		elif char == ']':
			hypernet_area = False
		else:
			test = ip_string[idx:idx+3]
			if hypernet_area and abasequence(test):
				aba = test[1] + test[:2]
				if aba in abas:
					return True
	return False

def abasequence(input):
	if len(input) != 3:
		return False
	good_chars = '[' not in input and ']' not in input
	aba = input[0] == input[2] and input[0] != input[1]
	return aba and good_chars

assert abasequence('aba')
assert abasequence('bcb')
assert not abasequence('aaa')
assert not abasequence('abc')
assert supportsSSL('aba[bab]xyz')
assert not supportsSSL('xyx[xyx]xyx')
assert supportsSSL('aaa[kek]eke')
assert supportsSSL('zazbz[bzb]cdb')

count2 = 0
filename = 'day07.txt'
with open(filename) as f:
	for line in f:
		if supportsSSL(line.strip('\n')):
			count2 += 1

print "Ip addresses in Part 2 that support SSL:", count2