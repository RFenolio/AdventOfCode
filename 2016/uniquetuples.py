# """[1,1],[2,2],[3,3],[4,4]
# [2,3],[1,4],[4,1],[3,2]
# [3,4],[4,3],[1,2],[2,1]
# [4,2],[3,1],[2,4],[1,3]
# For integer n>=4, write a function that will return a 2-dimensional NxN array satisfying following conditions: 
# 1) each element of the array will be a pair of integers [i,j] where i and j are 1...N 
# 2) no pair will be used more than once in resulting 2-dimensional array (e.g. pairs [1,2] and [2,1] are different, but [2,3] and [2,3] are equal) 
# 3) each column and row will have all numbers 1...N on both left sides of all pairs in that column/row and right sides of that column/row
# """

# def makeSquare(n):
# 	nums = makeOffsets(n)
# 	return [[makeTuple(x, y, n, nums) for x in range(n)] for y in range(n)]

# def makeTuple(x, y, n, offsets):
# 	new_x = (x + y) % n
# 	new_y = ((x + offsets[y]) % n)
# 	return (new_x, new_y)

# def makeOffsets(n):
# 	return range(0, n, 2) + range(1, n, 2)

def makeSquare(n):
    return [[(((x + y) % n), ((x +(y-1 if y == n-1  else (y * 2) % n)) % n)) for x in range(n)] for y in range(n)]

# def makeSquare(n):
#     return [[(((x + y) % n), ((x + (range(0, n, 2) + range(1, n, 2))[y]) % n)) for x in range(n)] for y in range(n)]

def verifySquare(square):
	pairs = [item for sublist in square for item in sublist]
	if len(pairs) != len(set(pairs)):
		return False
	# check rows
	if not checkRows(square):
		return False
	# check cols
	if not checkRows(zip(*square)):
		return False
	return True

def checkRows(square):
	for line in square:
		list1, list2 = zip(*line)
		if sorted(list1) != range(len(list1)) or sorted(list2) != range(len(list2)):
			return False
	return True


for n in range(1, 300, 2):
	a = makeSquare(n)
	print n, verifySquare(a)
# for line in a:
# 	print line

# # [ [[1,1],[2,2],[3,3],[4,4],[5,5]],
# #   [[2,3],[3,4],[4,5],[5,1],[1,2]],
# #   [[3,5],[4,1],[5,2],[1,3],[2,4]],
# #   [[4,2],[5,3],[1,4],[2,5],[3,1]],
# #   [[5,4],[1,5],[2,1],[3,2],[4,3]] ]

# def makeOffsets(n):
# 	return [n-1 if x == n-1 else (x*2)%(n-1) for x in range(n)]
# print makeOffsets(13)