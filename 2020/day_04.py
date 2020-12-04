
import re

from pprint import pprint
with open("day_04.txt") as f:
	passport_raw_data = f.read().splitlines()

with open("day_04_test1.txt") as f:
	test_data = f.read().splitlines()

def parse_line(line):
	return dict(item.split(":") for item in line.split())

assert (parse_line("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd") == 
	{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd'})

def make_passports(raw_data):
	passports = []
	passport = {}
	for line in raw_data:
		if line:
			passport.update(parse_line(line))
		else:
			passports.append(passport)
			passport = {}
	if passport:
		passports.append(passport)
	return passports

test_passports = make_passports(test_data)
assert len(test_passports) == 4

def validate_passport_1(passport):
	return (
		"byr" in passport
		and "iyr" in passport
		and "eyr" in passport
		and "hgt" in passport
		and "hcl" in passport
		and "ecl" in passport
		and "pid" in passport)

assert validate_passport_1(test_passports[0]) == True
assert validate_passport_1(test_passports[1]) == False
assert validate_passport_1(test_passports[2]) == True
assert validate_passport_1(test_passports[3]) == False

# Part 1
passports = make_passports(passport_raw_data)
valid_passports = [passport for passport in passports if validate_passport_1(passport)]
print("Part 1:", len(valid_passports))

# Part 2
def validate_height(passport):
	if "hgt" not in passport:
		return False
	hgt = passport["hgt"]
	is_num = hgt[:-2].isdigit()
	is_cm = hgt[-2:] == "cm"
	is_in = hgt[-2:] == "in"
	if is_num and is_cm:
		valid_height = 150 <= int(hgt[:-2]) <= 193
	elif is_num and is_in:
		valid_height = 59 <= int(hgt[:-2]) <= 76
	else: 
		valid_height = False
	return is_num and (is_cm or is_in) and valid_height

assert validate_height({"hgt":"60in"})
assert validate_height({"hgt":"190cm"})
assert not validate_height({"hgt":"190in"})
assert not validate_height({"hgt":"190"})

def validate_hair_color(passport):
	if "hcl" not in passport:
		return False
	hcl = passport["hcl"]
	return bool(re.search(r'^\#[0-9a-f]{6}$', hcl))

assert validate_hair_color({"hcl":"#123abc"})
assert not validate_hair_color({"hcl":"#123ac"})
assert not validate_hair_color({"hcl":"#123abz"})
assert not validate_hair_color({"hcl":"123abc"})

def validate_eye_color(passport):
	if "ecl" not in passport:
		return False
	return passport['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

assert validate_eye_color({"ecl":"brn"})
assert not validate_eye_color({"ecl":"wat"})

def validate_passport_id(passport):
	if "pid" not in passport:
		return False
	pid = passport["pid"]
	return len(pid) == 9 and pid.isdigit

assert validate_passport_id({"pid":"000000001"})
assert not validate_passport_id({"pid":"0123456789"})

def validate_passport_2(passport):
	return (
		"byr" in passport
		and "iyr" in passport
		and "eyr" in passport
		and "hgt" in passport
		and "hcl" in passport
		and "ecl" in passport
		and "pid" in passport
		and passport["byr"].isdigit() and 1920 <= int(passport["byr"]) <= 2002
		and passport["iyr"].isdigit() and 2010 <= int(passport["iyr"]) <= 2020
		and passport["eyr"].isdigit() and 2020 <= int(passport["eyr"]) <= 2030
		and validate_height(passport)
		and validate_hair_color(passport)
		and validate_eye_color(passport)
		and validate_passport_id(passport)
		)

test_data_2 = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

test_data_3 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

invalid_test_passports = make_passports(test_data_2.split("\n"))
assert not any(validate_passport_2(passport) for passport in invalid_test_passports)

valid_test_passports = make_passports(test_data_3.split("\n"))
assert all(validate_passport_2(passport) for passport in valid_test_passports)

valid_passports_part2 = [passport for passport in passports if validate_passport_2(passport)]
print("Part 2:", len(valid_passports_part2))




