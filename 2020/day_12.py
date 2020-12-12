with open("day_12.txt") as f:
	actions = f.read().splitlines()

FACINGS = ["N", "E", "S", "W"]
facing = 1

DIRECTIONS = {
	"N": [-1, 0],
	"E": [0, 1],
	"S": [1, 0],
	"W": [0, -1]
}

class Ship:
	def __init__(self):
		self.facing = 1
		self.loc = [0, 0]

	def turn_left(self, degrees):
		self.facing = (self.facing - (degrees // 90)) % 4
	
	def turn_right(self, degrees):
		self.facing = (self.facing + (degrees // 90)) % 4

	def move(self, distance, direction=None):
		if direction is None or direction == "F":
			# print(self.facing)
			direction = FACINGS[self.facing]
		x, y = DIRECTIONS[direction]
		self.loc = [(self.loc[0] + (x * distance)), (self.loc[1] + (y * distance))]

	def perform_action(self, action):
		distance = action[1:]
		action = action[0]
		distance = int(distance)
		if action in "NSEWF":
			self.move(distance, action)
		elif action == "L":
			self.turn_left(distance)
		elif action == "R":
			self.turn_right(distance)
		else:
			print("Danger!")


ship = Ship()
for action in actions:
	ship.perform_action(action)
print("Part 1:", sum(abs(x) for x in ship.loc))

class WaypointShip(Ship):
	def __init__(self):
		self.waypoint = [-1, 10]
		self.loc = [0, 0]
		self.facing = 1

	def rotate_waypoint(self, direction, distance):
		dist = distance // 90
		for _ in range(dist):
			if direction == "R":
				self.waypoint = [self.waypoint[1], -self.waypoint[0]]
			else:
				self.waypoint = [-self.waypoint[1], self.waypoint[0]]

	def move_to_waypoint(self, distance):
		x, y = self.waypoint
		self.loc = [(self.loc[0] + (x * distance)), (self.loc[1] + (y * distance))]

	def move_waypoint(self, direction, distance):
		x, y = DIRECTIONS[direction]
		self.waypoint = [self.waypoint[0] + distance * x, self.waypoint[1] + distance * y]

	def perform_action(self, action):
		act = action[0]
		dist = action[1:]
		dist = int(dist)
		if act in "NSEW":
			self.move_waypoint(act, dist)
		elif act == "F":
			self.move_to_waypoint(dist)
		elif act in "LR":
			self.rotate_waypoint(act, dist)
		else:
			print("Danger part 2!")

wp_ship = WaypointShip()
for action in actions:
	wp_ship.perform_action(action)
print("Part 2:", sum(abs(x) for x in wp_ship.loc))






