"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
"""
import unittest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for ch in s:
            if ch == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(ch)

        for ch in t:
            if ch == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(ch)

        s_str = ''.join(s_stack)
        t_str = ''.join(t_stack)

        if s_str == t_str:
            return True
        else:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.backspaceCompare("ab#c","ad#c"))

    def test_case2(self):
        self.assertFalse(self.obj.backspaceCompare("a#c","b"))

    def test_case3(self):
        self.assertTrue(self.obj.backspaceCompare("ab##","c#d#"))

    def test_case4(self):
        self.assertTrue(self.obj.backspaceCompare("y#fo##f","y#f#o##f"))