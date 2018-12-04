test_input = 3

start_buffer = [0]

def insert_val(buff, idx, step):
	next_loc = ((idx + step) % len(buff)) + 1
	buff.insert(next_loc, len(buff))
	return buff, next_loc

buff = start_buffer[:]
idx = 0
for _ in range(2017):
	buff, idx = insert_val(buff, idx, 335)

print(buff[(idx+1) % len(buff)])

# buff = start_buffer[:]
# idx = 0
# for _ in range(50000000):
# 	buff, idx = insert_val(buff, idx, 335)

# zero = buff.index(0)
# print buff[(idx + 1) % len(buff)]

from collections import deque

puzzle = 335
spinlock = deque([0])

for i in range(1, 50000001):
    spinlock.rotate(-puzzle)
    spinlock.append(i)

print(spinlock[spinlock.index(0) + 1])
