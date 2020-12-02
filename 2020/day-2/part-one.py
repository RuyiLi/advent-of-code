# |
# | Author: Ruyi Li
# | AOC 2020 Day 2 Part 1
# |

# | python part-one.py < input.txt

import sys

passwords = sys.stdin.read().split('\n')[:-1]

c = 0
for password in passwords:
	policy, pwd = password.split(': ')
	range, chr = policy.split()
	mn, mx = map(int, range.split('-'))
	if mn <= pwd.count(chr) <= mx:
		c += 1

print(c)
