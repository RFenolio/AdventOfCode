import os
import sys
import string

def get_input():
    input_file = os.path.join(sys.path[0], "day01_input.txt")
    with open(input_file) as f:
        return f.readlines()

data = get_input()

def get_number(line):
    digits = [char for char in line if char in string.digits]
    num = int(digits[0] + digits[-1])
    return num

example = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]
assert get_number(example[0]) == 12
assert get_number(example[1]) == 38

assert sum(get_number(line) for line in example) == 142

# Part 1:

print("Part 1: ", sum(get_number(line) for line in data))

# Part 2:

example2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]
tokens = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_first(line):
    idx = float('inf')
    val = ''
    for token in tokens.keys():
        location = line.find(token)
        if location != -1 and location < idx:
            idx = location
            val = token
    return tokens[val]

def get_last(line):
    idx = -1
    val = ''
    for token in tokens.keys():
        location = line.rfind(token)
        if location > idx:
            idx = location
            val = token
    return tokens[val]

def get_val(line):
    return int(get_first(line) + get_last(line))


assert sum(get_val(line) for line in example2) == 281
print('Part 2: ', sum(get_val(line) for line in get_input()))

# print(get_val('nineseven2sixnineqd'))
# for line in data[:100]:
#     res = get_val(line)
#     if res > 90:
#         print(get_val(line), " - ", line.rstrip('\n'))