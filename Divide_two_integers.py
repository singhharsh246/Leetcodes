"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        flag = 0
        flag2 = 0
        if(dividend == divisor):
            flag2 = 1
        elif(dividend != divisor and abs(dividend) == abs(divisor)):
            flag2 = 2
        try:
            if ((dividend /  abs(dividend)) !=  (divisor /  abs(divisor)) ) :

                dividend = abs(dividend)
                divisor = abs(divisor)
                flag = 1
        except:
            pass

        number = 0
        if(flag2 == 1):
            number = 1
            return(number)
        elif(flag2 == 2):
            number = -1
            return(number)

        dummy = abs(divisor)
        while (abs(dividend) >= dummy):
            number += 1
            dummy += divisor
            #print("here", dummy, number)

        if (flag == 1):
            number *= -1
            return(number)

        if (number > (2**31 - 1)):
            number = 2**31 - 1
        elif (number < - (2**31)):
            number = - (2**31)

        return(number)
