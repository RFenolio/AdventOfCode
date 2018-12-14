from typing import List, Tuple

def parse_input(filename: str) => Tuple[str, List[str]]:
	with open(filename) as f:
		res = f.read().splitlines()
	pots = res[0][15:]
	notes = res[2:]
	return pots, notes

def parse_note(note: str) => List[str]:
	return note.split(' => ')

def parse_notes(notes: List[str]) => List[List[str]]:
	return [parse_note(note) for note in notes]




