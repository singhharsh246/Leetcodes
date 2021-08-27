
"""

Given a string s,
determine if it is a palindrome,
considering only alphanumeric
characters and ignoring cases.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = ("").join((i.lower() for i in s if i.isalnum()))

        if (data == data[::-1]):
            return True
        else:
            return False