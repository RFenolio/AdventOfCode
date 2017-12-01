targets = {
	"bots": {},
	"outputs": {},
}
starting_instructions = []

def parse_instruction(str):
	parts = str.split(' ')
	if parts[0] == 'value':
		starting_instructions.append((parts[1], parts[5]))
	else:
		num = parts[1]
		low = (parts[5], parts[6])
		high = (parts[10], parts[11])
		targets['bots'][num] = bot(num, low, high)

class bot():
	def __init__(self, num, low, high):
		self.num = num
		self.low = low
		self.high = high
		self.chips = []

	def __str__(self):
		return "Num: %s, chips: %s" % (self.num, str(self.chips))

	def get_chip(self, chip):
		self.chips.append(int(chip))
		if len(self.chips) == 2:
			chips = sorted(self.chips)
			if 17 in chips and 61 in chips:
				print "bot %s is responsible for comparing the chips" % self.num
			self.give_chip(self.low, chips[0])
			self.give_chip(self.high, chips[1])
			self.chips = []

	def give_chip(self, target, chip):
		if target[0] == 'output':
			targets['outputs'][target[1]] = targets['outputs'].get(target[1], [])
			targets['outputs'][target[1]].append(chip)
		if target[0] == 'bot':
			targets['bots'][target[1]].get_chip(chip)


filename = "day10.txt"
with open(filename) as f:
	for line in f:
		parse_instruction(line.strip('\n'))

for inst in starting_instructions:
	targets['bots'][inst[1]].get_chip(inst[0])

print "product of values in outputs 0, 1, and 2: ", (targets['outputs']['0'][0] * targets['outputs']['1'][0] * targets['outputs']['2'][0])








