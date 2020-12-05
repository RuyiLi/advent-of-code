import sys
import re
from operator import itemgetter

re_attrs = re.compile(r'(\w{3}):([^\n\s]+)')
re_hex = re.compile(r'#[0-9a-f]{6}')

lines = sys.stdin.read().split('\n\n')
lines = [dict(re.findall(re_attrs, passport)) for passport in lines]


def validate_height(val: str) -> bool:
	try:
		val, unit = int(val[:-2]), val[-2:]

		if unit == 'cm':
			return 150 <= val <= 193

		if unit == 'in':
			return 59 <= val <= 76

	except ValueError:
		pass

	return False


reqs = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


c = 0
for passport in lines:
	try:
		byr, iyr, eyr, hgt, hcl, ecl, pid = itemgetter(*reqs)(passport)
		c += int(
			1920 <= int(byr) <= 2002 and
			2010 <= int(iyr) <= 2020 and
			2020 <= int(eyr) <= 2030 and
			validate_height(hgt) and
			re.match(re_hex, hcl) is not None and
			ecl in eye_colors and
			pid.isdigit() and
			len(pid) == 9
		)
	except KeyError:
		pass

print(c)
