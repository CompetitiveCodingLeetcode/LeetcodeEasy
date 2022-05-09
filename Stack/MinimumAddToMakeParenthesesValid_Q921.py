"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.



Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3


Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'
"""
import unittest


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')' and len(stack) !=0:
                stack.pop()
            else:
                count += 1
        if len(stack) != 0:
            count += len(stack)
        return count

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.minAddToMakeValid("())"),1)

    def test_case2(self):
        self.assertEqual(self.obj.minAddToMakeValid(")))"),3)