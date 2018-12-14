class Recipe:
	def __init__(self, score, idx):
		self.idx = idx
		self.score = score
		self.next = None
		self.prev = None
	
	def __repr__(self):
		if self.next is None:
			return str(self.score)
		return str(self.score) + self.next.__repr__()

	def left_vals(self, num: int):
		current = self
		vals = []
		for _ in range(num):
			if current.prev is not None:
				vals.append(str(current.score))
				current = current.prev
		return ''.join(vals[::-1])



class Elf:
	def __init__(self, id, recipes):
		self.recipes = recipes # keep track of the start of the list
		self.id = id
		self.current = None

	def move(self):
		distance = self.current.score + 1
		for _ in range(distance):
			if self.current.next is None:
				self.current = self.recipes
			else:
				self.current = self.current.next


def setup():
	recipe_list = Recipe(score=3, idx=1)
	recipe_list.next = Recipe(score=7, idx=2)
	recipe_list.next.prev = recipe_list
	elf1 = Elf(1, recipe_list)
	elf1.current = recipe_list
	elf2 = Elf(2, recipe_list)
	elf2.current = recipe_list.next
	return recipe_list, elf1, elf2

def make_new(s1: int, s2: int, recipe: Recipe):
	val = s1 + s2
	for numeral in str(val):
		assert recipe.next is None
		recipe.next = Recipe(int(numeral), recipe.idx+1)
		recipe.next.prev = recipe
		recipe = recipe.next

def make_and_move(e1, e2, end):
	make_new(e1.current.score, e2.current.score, end)
	e1.move()
	e2.move()

def experiment(num_recipes: int):
	recipes, elf1, elf2 = setup()
	end = recipes.next
	# print(recipes)
	while end.idx < num_recipes + 10:
		make_and_move(elf1, elf2, end)
		while end.next is not None:
			end = end.next
			if end.idx == num_recipes + 1:
				target = end
	# print(recipes)
	# print(elf1.current.idx, elf1.current.score)
	# print(elf2.current.idx, elf2.current.score)
	# print(f"idx of end: {end.idx}")
	return (str(target)[:10])

# Part 1
# print(experiment(30121))


# Part 2
def experiment2(target: str):
	recipes, elf1, elf2 = setup()
	end = recipes.next
	while end.idx < 30000000:
		make_and_move(elf1, elf2, end)
		while end.next is not None:
			end = end.next
			if end.left_vals(len(target)) == target:
				return end.idx - len(target)
			# if end.idx > 2000:
			# 	print(end.idx, end.left_vals(len(target)))
	return "oops! didn't find anything"


assert experiment2('51589') == 9
assert experiment2('01245') == 5
assert experiment2('92510') == 18
assert experiment2('59414') == 2018

print(experiment2('030121'))






