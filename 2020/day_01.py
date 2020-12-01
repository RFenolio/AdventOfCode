with open("day_01.txt") as f:
	expense_report = [int(line) for line in f.readlines()]

checked = set()
total = 2020

print("Part 1")
# dict solution
for num in expense_report:
	if (checking := (total - num)) in checked:
		print (checking * num)
	else:
		checked.add(num)

print("Part 2")
# brute force part 2, the list is short enough
for num1 in expense_report:
	for num2 in expense_report:
		for num3 in expense_report:
			if sum((num1, num2, num3)) == 2020:
				print(num1, num2, num3)
				print(num1 * num2 * num3)