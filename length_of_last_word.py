"""

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string_list = s.split()
        length_word = len(string_list[len(string_list) - 1])
        return(length_word)