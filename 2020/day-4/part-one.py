import sys
import re

re_attrs = re.compile(r'(\w{3}):[^\n\s]+')

lines = sys.stdin.read().split('\n\n')
lines = [re.findall(re_attrs, passport) for passport in lines]

reqs = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

c = 0
for passport in lines:
	if all(attr in passport for attr in reqs):
		c += 1

print(c)
