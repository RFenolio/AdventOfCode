import os
import sys

"""
Get data 
"""
input_file = os.path.join(sys.path[0], "day04_input.txt")
with open(input_file) as f:
    puzzle_input = f.read()
    
test_input_file = os.path.join(sys.path[0], "day04_test_input.txt")
with open(test_input_file) as f:
    puzzle_test_input = f.read()

def parse_input(puzzle: str):
    puzzle_parts = puzzle.split("\n\n")
    draw_numbers = [int(val) for val in puzzle_parts[0].split(',')]
    cards = puzzle_parts[1:]
    return draw_numbers, cards

"""
Part 1
"""
class Card():
    def __init__(self, card_input):
        self.board = [[int(val) for val in row.split()] for row in card_input.split('\n')]
    
    def mark(self, drawn_number):
        self.board = [
            [-1 if val == drawn_number else val for val in row] 
            for row in self.board
        ]
        self.last_val = drawn_number
    
    def check_rows(self):
        return any(
            all(val == -1 for val in row)
            for row in self.board
        )

    def check_cols(self):
        return any(
            all(val == -1 for val in row)
            for row in zip(*self.board)
        )
    
    def check_card(self):
        return self.check_rows() or self.check_cols()
    
    def score(self):
        board_sum = sum(sum(val for val in row if val != -1) for row in self.board)
        return board_sum * self.last_val
        
test_game = parse_input(puzzle_test_input)
test_card = Card(test_game[1][2])
for val in test_game[0][:12]:
    test_card.mark(val)
assert test_card.score() == 4512

def play_bingo(puzzle_input):
    vals, card_vals = parse_input(puzzle_input)
    cards = [Card(card) for card in card_vals]
    for val in vals:
        for card in cards:
            card.mark(val)
            if card.check_card():
                return card.score()

assert play_bingo(puzzle_test_input) == 4512
print("Part 1:", play_bingo(puzzle_input))


"""
Part 2
"""
def find_loser(puzzle_input):
    vals, card_vals = parse_input(puzzle_input)
    cards = [Card(card) for card in card_vals]
    while len(cards) > 1:
        next_val = vals.pop(0)
        for card in cards:
            card.mark(next_val)
        cards = [card for card in cards if not card.check_card()]
    loser = cards[0]
    while not loser.check_card():
        loser.mark(vals.pop(0))
    return loser.score()

assert find_loser(puzzle_test_input) == 1924
print("Part 2:", find_loser(puzzle_input))


