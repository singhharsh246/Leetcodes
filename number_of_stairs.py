"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0

        if n == 1:
            return 1
        if n == 2:
            return 2

        for i in range(0, n+1):
            j = 0
            if 2*i <= n:
                j = n - 2*i
            else:
                return total

            total += comb(i+j, i)
            print(i, j, total)