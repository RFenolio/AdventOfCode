import os
import sys
from math import prod
from typing import List, Set, Tuple
from statistics import median

"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day10_input.txt")
with open(input_file) as f:
    puzzle = f.read().splitlines()

input_file = os.path.join(sys.path[0], "day10_test_input.txt")
with open(input_file) as f:
    test_puzzle = f.read().splitlines()

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    '0': 0,
    '1': 1
}

def check_line(line):
    opens = []
    for char in line:
        if char in "([{<":
            opens.append(char)
        else:
            opener = opens.pop()
            if pairs[opener] != char:
                return char, opens
    if opens:
        return '0', opens
    return '1', opens

assert check_line('{()()()}')[0] == '1'

def error_score(puzzle):
    return(sum(scores[check_line(line)[0]] for line in puzzle))

assert error_score(test_puzzle) == 26397
print('Part 1:', error_score(puzzle))

def complete_line(leftovers):
    return "".join(pairs[char] for char in leftovers[::-1])

_, leftovers1 = check_line('[({(<(())[]>[[{[]{<()<>>')
assert complete_line(leftovers1) == '}}]])})]'
_, leftovers2 = check_line('<{([{{}}[<[[[<>{}]]]>[]]')
autocomplete2 = complete_line(leftovers2)
assert autocomplete2 == '])}>'
autocomplete_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def autocomplete_score(leftovers):
    score = 0
    for char in leftovers:
        score = score * 5 + autocomplete_scores[char]
    return score

assert autocomplete_score(autocomplete2) == 294

def autocomplete_winner(input):
    leftovers = [check_line(line)[1] for line in input if check_line(line)[0] == '0']
    scores = [autocomplete_score(complete_line(leftover)) for leftover in leftovers]
    scores.sort
    return median(scores)

assert autocomplete_winner(test_puzzle) == 288957
print('Part 2:', autocomplete_winner(puzzle))

