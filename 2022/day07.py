import re
import os
import sys

input_file = os.path.join(sys.path[0], "day07_input.txt")
with open(input_file) as f:
	puzzle_input = f.read().splitlines()

def calculate_sizes(commands):
    size = 0
    folders = []
    all_folders = []
    while(True):
        match next(commands, "$ cd ..").split():
            case "$", "ls":
                pass
            case "dir", directory:
                pass
            case "$", "cd", "..":
                if size <= 100000:
                    folders.append(size)
                all_folders.append(size)
                return size, folders, all_folders
            case "$", "cd", _:
                dir_size, folder_list, all_folders_list = calculate_sizes(commands)
                size += dir_size
                folders.extend(folder_list)
                all_folders.extend(all_folders_list)
            case filesize, _:
                size += int(filesize)
                
part1_total, part1_folders, all_folders = calculate_sizes(iter(puzzle_input))
print("Part 1:", sum(part1_folders))

# Part 2
drive_size = 70000000
remaining = drive_size - part1_total
size_needed = 30000000
candidate_folders = [folder for folder in all_folders if folder > (size_needed - remaining)]
print("Part 2:", min(candidate_folders))