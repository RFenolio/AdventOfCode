# PART 1

PUZZLE_INPUT = """DLRURUDLULRDRUDDRLUUUDLDLDLRLRRDRRRLLLLLDDRRRDRRDRRRLRRURLRDUULRLRRDDLULRLLDUDLULURRLRLDUDLURURLDRDDULDRDRDLDLLULULLDDLRRUDULLUULRRLLLURDRLDDLDDLDRLRRLLRURRUURRRRLUDLRDDDDRDULRLLDDUURDUDRLUDULLUDLUDURRDRDUUUUDDUDLLLRLUULRUURDLRLLRRLRLLDLLRLLRRRURLRRLURRLDLLLUUDURUDDLLUURRDRDRRDLLDDLLRDRDRRLURLDLDRDLURLDULDRURRRUDLLULDUDRURULDUDLULULRRRUDLUURRDURRURRLRRLLRDDUUUUUDUULDRLDLLRRUDRRDULLLDUDDUDUURLRDLULUUDLDRDUUUDDDUDLDURRULUULUUULDRUDDLLLDLULLRLRLUDULLDLLRLDLDDDUUDURDDDLURDRRDDLDRLLRLRR
RLDUDURDRLLLLDDRRRURLLLRUUDDLRDRDDDUDLLUDDLRDURLDRDLLDRULDDRLDDDRLDRDDDRLLULDURRRLULDRLRDRDURURRDUDRURLDRLURDRLUULLULLDLUDUDRDRDDLDDDDRDURDLUDRDRURUDDLLLRLDDRURLLUDULULDDLLLDLUDLDULUUDLRLURLDRLURURRDUUDLRDDDDDRLDULUDLDDURDLURLUURDLURLDRURRLDLLRRUDRUULLRLDUUDURRLDURRLRUULDDLDLDUUDDRLDLLRRRUURLLUURURRURRLLLUDLDRRDLUULULUDDULLUDRLDDRURDRDUDULUDRLRRRUULLDRDRLULLLDURURURLURDLRRLLLDRLDUDLLLLDUUURULDDLDLLRRUDDDURULRLLUDLRDLUUDDRDDLLLRLUURLDLRUURDURDDDLLLLLULRRRURRDLUDLUURRDRLRUDUUUURRURLRDRRLRDRDULLDRDRLDURDDUURLRUDDDDDLRLLRUDDDDDURURRLDRRUUUDLURUUDRRDLLULDRRLRRRLUUUD
RDRURLLUUDURURDUUULLRDRLRRLRUDDUDRURLLDLUUDLRLLDDURRURLUDUDDURLURLRRURLLURRUDRUDLDRLLURLRUUURRUDDDURRRLULLLLURDLRLLDDRLDRLLRRDLURDLRDLDUDRUULLDUUUDLURRLLRUDDDUUURLURUUDRLRULUURLLRLUDDLLDURULLLDURDLULDLDDUDULUDDULLRDRURDRRLLDLDDDDRUDLDRRLLLRLLLRRULDLRLRLRLLDLRDRDLLUDRDRULDUURRDDDRLLRLDLDRDUDRULUDRDLDLDDLLRULURLLURDLRRDUDLULLDLULLUDRRDDRLRURRLDUDLRRUUDLDRLRLDRLRRDURRDRRDDULURUUDDUUULRLDRLLDURRDLUULLUDRDDDLRUDLRULLDDDLURLURLRDRLLURRRUDLRRLURDUUDRLRUUDUULLRUUUDUUDDUURULDLDLURLRURLRUDLULLULRULDRDRLLLRRDLU
RRRRDRLUUULLLRLDDLULRUUURRDRDRURRUURUDUULRULULRDRLRRLURDRRRULUUULRRUUULULRDDLLUURRLLDUDRLRRLDDLDLLDURLLUDLDDRRURLDLULRDUULDRLRDLLDLRULLRULLUDUDUDDUULDLUUDDLUDDUULLLLLURRDRULURDUUUDULRUDLLRUUULLUULLLRUUDDRRLRDUDDRULRDLDLLLLRLDDRRRULULLLDLRLURRDULRDRDUDDRLRLDRRDLRRRLLDLLDULLUDDUDDRULLLUDDRLLRRRLDRRURUUURRDLDLURRDLURULULRDUURLLULDULDUDLLULDDUURRRLDURDLUDURLDDRDUDDLLUULDRRLDLLUDRDURLLDRLDDUDURDLUUUUURRUULULLURLDUUULLRURLLLUURDULLUULDRULLUULRDRUULLRUDLDDLRLURRUUDRLRRRULRUUULRULRRLDLUDRRLL
ULRLDLLURDRRUULRDUDDURDDDLRRRURLDRUDDLUDDDLLLRDLRLLRRUUDRRDRUULLLULULUUDRRRDRDRUUUUULRURUULULLULDULURRLURUDRDRUDRURURUDLDURUDUDDDRLRLLLLURULUDLRLDDLRUDDUUDURUULRLLLDDLLLLRRRDDLRLUDDUULRRLLRDUDLLDLRRUUULRLRDLRDUDLLLDLRULDRURDLLULLLRRRURDLLUURUDDURLDUUDLLDDRUUDULDRDRDRDDUDURLRRRRUDURLRRUDUDUURDRDULRLRLLRLUDLURUDRUDLULLULRLLULRUDDURUURDLRUULDURDRRRLLLLLUUUULUULDLDULLRURLUDLDRLRLRLRDLDRUDULDDRRDURDDULRULDRLRULDRLDLLUDLDRLRLRUDRDDR"""


class bathroom_code():
	def __init__(self, keypad, instructions):
		"""
		keypad should be a 2D array of the keypad with strings for each character
		instructions are a single string with each line representing a set of instructions
		"""
		self.keypad = keypad
		self.loc = self.get_starting_location()
		self.combination = ''
		self.instructions = instructions.split('\n')

	def find_code(self):
		if self.combination == '':
			for sequence in self.instructions:
				self.get_next_location(sequence)
		return self.combination

	def get_starting_location(self):
		for idx, keypad_row in enumerate(self.keypad):
			if '5' in keypad_row:
				return [idx, keypad_row.index('5')]

	def get_next_location(self, sequence):
		"""Start is a coordinate on the keypad"""
		for char in sequence:
			self.move(char)
		next_key = self.keypad[self.loc[0]][self.loc[1]]
		self.combination += next_key

	def move(self, direction):
		if direction == "U":
			if self.loc[0] > 0 and self.keypad[self.loc[0] - 1][self.loc[1]] != 'X':
				self.loc[0] -= 1
		elif direction == "L":
			if self.loc[1] > 0 and self.keypad[self.loc[0]][self.loc[1] - 1] != 'X':
				self.loc[1] -= 1
		elif direction == "D":
			if self.loc[0] < len(self.keypad) - 1 and self.keypad[self.loc[0] + 1][self.loc[1]] != 'X':
				self.loc[0] += 1
		elif direction == "R":
			if self.loc[1] < len(self.keypad[0]) - 1 and self.keypad[self.loc[0]][self.loc[1] + 1] != 'X':
				self.loc[1] += 1

PART1_KEYPAD = [
	['1', '2', '3'],
	['4', '5', '6'],
	['7', '8', '9'],
]

TEST_INSTRUCTIONS = """ULL
RRDDD
LURDL
UUUUD"""

test1 = bathroom_code(PART1_KEYPAD, TEST_INSTRUCTIONS)
test1.find_code()
assert test1.combination == '1985'

part1 = bathroom_code(PART1_KEYPAD, PUZZLE_INPUT)
part1.find_code()
print "Part 1 bathroom combination:", part1.combination


# PART 2
PART2_KEYPAD = [
['X', 'X', '1', 'X', 'X'],
['X', '2', '3', '4', 'X'],
['5', '6', '7', '8', '9'],
['X', 'A', 'B', 'C', 'X'],
['X', 'X', 'D', 'X', 'X'],
]

test2 = bathroom_code(PART2_KEYPAD, TEST_INSTRUCTIONS)
test2.find_code()
assert test2.combination == "5DB3"


part1 = bathroom_code(PART2_KEYPAD, PUZZLE_INPUT)
part1.find_code()
print "Part 2 bathroom combination:", part1.combination








