from math import prod

earliest = 1001796
departures = "37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,457,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,431,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19".split(",")


# earliest = 939
# departures = "7,13,x,x,59,x,31,19".split(',')
# bus = 59
# early = 939
# departure = early // bus
# departure *= bus
# if departure < 939:
# 	departure += bus
# print(departure)

min_bus = None
min_time = 100000000000000000
for bus in departures:
	if bus == "x":
		continue
	bus = int(bus)
	departure_time = earliest // bus
	# print (departure_time)
	departure_time *= bus
	if departure_time < earliest:
		departure_time += bus
	# print(bus,departure_time)
	if departure_time < min_time:
		min_time = departure_time
		min_bus = bus

part_1 = min_bus * (min_time - earliest)
print("Part 1:", min_bus * (min_time - earliest))

equations = ", ".join([f"(x+{idx}) mod {bus} == 0" for idx, bus in enumerate(departures) if bus != "x"])
print("Part 2:",equations)
