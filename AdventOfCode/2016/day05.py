from hashlib import md5
from random import randint
idx = 0
seed = 'abbhdwsy'
password = [False, False, False, False, False, False, False, False]
while False in password:
	m = md5(seed)
	m.update(str(idx))
	digest = m.hexdigest()
	if digest[:5] == "00000":
		pos = digest[5]
		val = digest[6]
		if pos in '01234567' and not password[int(pos)]:
			password[int(pos)] = val
			print password
	idx += 1
print "".join(password)