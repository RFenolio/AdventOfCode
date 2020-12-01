with open('day08_input.txt') as f:
	data = f.read()


def split_layers(data, width, height):
	size = width * height
	return [data[n*size:n*size+size] for n in range(len(data)//size)]

parsed = split_layers(data, 25, 6)
fewest_zeroes = 150
layer_idx = None
for idx, layer in enumerate(parsed):
	zeros = layer.count('0')
	if zeros < fewest_zeroes:
		fewest_zeroes = zeros
		layer_idx = idx

print(parsed[layer_idx].count('1') * parsed[layer_idx].count('2'))
print("\n")

colors = list(''.join(item).strip('2')[0] for item in zip(*parsed))
image = [colors[n*25:n*25+25] for n in range(len(colors)//25)]
for line in image:
	print("".join(line).replace('0', ' '))

