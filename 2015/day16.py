from pprint import pprint

with open('day16.txt') as input:
	data = input.read()

results = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1,
	}

def process_line(str):
	sue = {}
	data = str.split(' ')
	sue['id'] = int(data[1].strip(':'))
	key1 = data[2].strip(':')
	key2 = data[4].strip(':')
	key3 = data[6].strip(':')
	vals = {}
	vals[key1] = int(data[3].strip(','))
	vals[key2] = int(data[5].strip(','))
	vals[key3] = int(data[7].strip(','))
	sue['vals'] = vals
	return sue

data = data.split('\n')
sues = [process_line(item) for item in data]

# part 1
for sue in sues:
	vals = sue['vals']
	valid = True
	for key in vals:
		if vals[key] != results[key]:
			valid = False
	if valid:
		print sue

# part 2
"""In particular, the cats and trees readings indicates that there 
are greater than that many (due to the unpredictable nuclear decay of 
cat dander and tree pollen), while the pomeranians and goldfish 
readings indicate that there are fewer than that many (due to the 
modial interaction of magnetoreluctance)."""
for sue in sues:
	vals = sue['vals']
	valid = True
	for key in vals:
		if key in ['cats', 'trees']:
			if vals[key] <= results[key]:
				valid = False
		elif key in ['pomeranians', 'goldfish']:
			if vals[key] >= results[key]:
				valid = False
		elif vals[key] != results[key]:
			valid = False
		else:
			pass
	if valid:
		print sue