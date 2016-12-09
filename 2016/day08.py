filename = 'day08.txt'

# Part 1

class Display():

	def __init__(self, width, height):
		self.display = [[' ' for _ in range(width)] for _ in range(height)]

	def __str__(self):
		return "\n".join([''.join([item for item in row]) for row in self.display])

	def addRectangle(self, width, height):
		for row in self.display[:height]:
			for x in range(width):
				row[x] = "#"

	def shiftRow(self, row, dist):
		for _ in range(dist):
			temp = self.display[row].pop()
			self.display[row].insert(0, temp)

	def shiftCol(self, col, dist):
		temp = []
		for row in self.display:
			temp.append(row[col])
		for _ in range(dist):
			temp.insert(0, temp.pop())
		for idx, row in enumerate(self.display):
			row[col] = temp[idx]

	def execute(self, str):
		parts = str.split(' ')
		if parts[0] == 'rect':
			self.addRectangle(*[int(val) for val in parts[1].split('x')])
		else:
			func = self.shiftRow if parts[1] == 'row' else self.shiftCol
			idx = int(parts[2].split('=')[1])
			dist = int(parts[4])
			func(idx, dist)

	def countPixels(self):
		return sum(row.count('#') for row in self.display)

display = Display(50, 6)
with open(filename) as f:
	for line in f:
		display.execute(line.strip())

print display
print display.countPixels()