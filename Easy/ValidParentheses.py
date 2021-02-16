"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(": ")", "{": "}", "[": "]"}
        opening_bracket = []
        index = 0
        for c in s:
            if c in bracket_dict:
                print("index=", index)
                opening_bracket.append(c)
                index += 1
            else:
                if index == 0:
                    return False
                if bracket_dict[opening_bracket[index - 1]] == c:
                    index -= 1
                    opening_bracket.pop(index)
                else:
                    return False
                    break
        if len(opening_bracket):
            return False
        return True




obj = Solution()
print(obj.isValid("["))
print(obj.isValid("]"))
print(obj.isValid("{[]}"))
print(obj.isValid("(]"))

