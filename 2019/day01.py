with open("day01_input.txt") as f:
	data = f.readlines()
	data = [int(val) for val in data]

def find_fuel(mass):
	return (mass // 3) - 2

assert find_fuel(12) == 2
assert find_fuel(14) == 2
assert find_fuel(1969) == 654
assert find_fuel(100756) == 33583

# ===== Part 1 =====
part1 = sum(find_fuel(mass) for mass in data)
print(part1)

# --- Part Two ---
def find_bonus_fuel(mass):
	total = 0
	fuel = find_fuel(mass)
	while fuel > 0:
		total += fuel
		fuel = find_fuel(fuel)
	return total

assert find_bonus_fuel(14) == 2
assert find_bonus_fuel(1969) == 966
assert find_bonus_fuel(100756) == 50346

part2 = sum(find_bonus_fuel(mass) for mass in data)
print(part2)