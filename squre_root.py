"""

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

"""


def squaring():
    current = 1

    while True:
        current += 1
        yield  (current-1)


class Solution:
    def mySqrt(self, x: int) -> int:

        squ = squaring()

        count = 0
        while count*count <= x:
            count = next(squ)

        return(count-1)