# |
# | Author: Ruyi Li
# | AOC 2020 Day 1 Part 1
# |

# | python part-one.py < day-1.in

import sys

nums = sys.stdin.read().split('\n')
nums = [int(num) for num in nums if num.isdigit()]

for a in nums:
	for b in nums:
		if a + b == 2020:
			print(a * b)
			sys.exit(0)
