# |
# | Author: Ruyi Li
# | AOC 2020 Day 1 Part 2
# |

# | python part-two.py < input.txt

import sys

nums = sys.stdin.read().split('\n')
nums = [int(num) for num in nums if num.isdigit()]

for a in nums:
	for b in nums:
		for c in nums:
			if a + b + c == 2020:
				print(a * b * c)
				sys.exit(0)
