# |
# | Author: Ruyi Li
# | AOC 2020 Day 2 Part 2
# |

# | python part-two.py < input.txt

import sys

passwords = sys.stdin.read().split('\n')[:-1]

c = 0
for password in passwords:
	policy, pwd = password.split(': ')
	indices, chr = policy.split()
	a, b = map(int, indices.split('-'))
	if (pwd[a - 1] == chr) ^ (pwd[b - 1] == chr):
		c += 1

print(c)
