"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

"""



class Solution:
    def isValid(self, s: str) -> bool:

        k = {
            "(": 0,
            ")": 1,
            "{": 2,
            "}": 3,
            "[": 4,
            "]": 5
        }

        l = list()

        for i, j in enumerate(s):
            if i == 0 and j in (")", "}", "]"):
                return False
            if j in ("(", "{", "["):
                l.append(k[j])

            else:
                if len(l) != 0:
                    if(l[len(l)-1] + 1 == k[j]):
                        l.pop()
                    else:
                        return False
                else:
                    l.append(k[j])
        if len(l) == 0:
            return True
        else:
            return False