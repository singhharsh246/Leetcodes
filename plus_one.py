"""

Runtime: 28 ms, faster than 88.45% of Python3 online submissions for Plus One.
Memory Usage: 14.3 MB, less than 48.36% of Python3 online submissions for Plus One.

"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if len(digits) == 1 and digits[0] == 0:
            digits[-1] += 1
            return(digits)
        digits = ("").join(str(i) for i in digits)
        digits = int(digits)
        digits += 1
        digits = str(digits)
        digits = list(digits)
        return(digits)
