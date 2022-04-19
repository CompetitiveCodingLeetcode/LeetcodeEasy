"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

APPROACH FOLLOWED: STACK
"""
import unittest


class Solution:
    def removeDuplicates(self, s: str) -> str:
        ptr = 0
        s_stack = []
        while ptr != len(s):
            if len(s_stack) == 0:
                s_stack.append(s[ptr])
                ptr += 1
            elif s_stack[-1] == s[ptr]:
                s_stack.pop()
                ptr += 1
            else:
                s_stack.append(s[ptr])
                ptr += 1
        s = ""
        while len(s_stack) != 0:
            s += s_stack.pop(0)

        return s

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.removeDuplicates("abbaca"),"ca")

    def test_case2(self):
        self.assertEqual(self.obj.removeDuplicates("azxxzy"),"ay")