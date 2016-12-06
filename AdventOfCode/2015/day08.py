import json
filename = "day08.txt"
raw_len = 0
decoded_len = 0
json_encoded_len = 0
with open(filename, "r") as f:
	for line in f:
		line = line.strip('\n')
		raw_len += len(line)
		decoded_len += len(line.decode('string-escape'))-2
		json_encoded_len += len(json.dumps(line))

print "raw_len:", raw_len
print "decoded_len:", decoded_len
print "json_encoded_len:", json_encoded_len
print "Part 1 answer:", raw_len - decoded_len
print "Part 2 answer:", json_encoded_len - raw_len
