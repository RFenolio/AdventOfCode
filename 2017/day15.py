

def gen(start, constant):
	num = start
	while True:
		num = (num * constant) % 2147483647
		yield num


gen_a = gen(116, 16807)
gen_b = gen(299, 48271)

test_a = gen(65, 16807)
test_b = gen(8921, 48271)

def calculate(gen1, gen2):
	return next(gen1) % 65536 == next(gen2) % 65536


# test_count = 0
# for _ in range(5):
# 	if calculate(test_a, test_b):
# 		test_count += 1
# print(test_count)

# count1 = 0
# for _ in range(40000000):
# 	if calculate(gen_a, gen_b):
# 		count1 += 1
# print(count1)


def gen2(start, constant, divisor):
	num = start
	while True:
		num = (num * constant) % 2147483647
		if num % divisor == 0:
			yield num

gen_a2 = gen2(116, 16807, 4)
gen_b2 = gen2(299, 48271, 8)

test_a2 = gen2(65, 16807, 4)
test_b2 = gen2(8921, 48271, 8)

# test_a2_count = 0
# for x in range(5000000):
# 	if calculate(test_a2, test_b2):
# 		test_a2_count +=1
# print(test_a2_count)

count2 = 0
for x in range(5000000):
	if calculate(gen_a2, gen_b2):
		count2 +=1
print(count2)

# print(8 & 7)
