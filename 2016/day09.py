filename = 'day09.txt'

def decode(str):
	result = ''
	marker = ''
	while len(str) > 0:
		if str[0] == '(':
			marker, str = str[1:].split(')', 1)
			dist, times = (int(x) for x in marker.split('x'))
			result += str[:dist] * times
			str = str[dist:]
		else:
			result += str[0]
			str = str[1:]
	return result

assert decode('ADVENT') == 'ADVENT'
assert decode('A(1x5)BC') == 'ABBBBBC'
assert decode('(3x3)XYZ') == 'XYZXYZXYZ'
assert decode('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert decode('(6x1)(1x3)A') == '(1x3)A'
assert decode('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

length = 0
with open(filename) as f:
	for line in f:
		length += len(decode(line.strip()))
print "length of decoded file:", length

def decode2(str):
	result = ''
	marker = ''
	while len(str) > 0:
		if str[0] == '(':
			marker, str = str[1:].split(')', 1)
			dist, times = (int(x) for x in marker.split('x'))
			result += decode2(str[:dist]) * times
			str = str[dist:]
		else:
			result += str[0]
			str = str[1:]
	return result

assert decode2('(3x3)XYZ') == 'XYZXYZXYZ'
assert decode2('X(8x2)(3x3)ABCY') == 'XABCABCABCABCABCABCY'
assert len(decode2('(27x12)(20x12)(13x14)(7x10)(1x12)A')) == 241920
assert len(decode2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')) == 445

length2 = 0
with open(filename) as f:
	for line in f:
		length2 += len(decode2(line.strip()))
print "length of decoded file:", length2
