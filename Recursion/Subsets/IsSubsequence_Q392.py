"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
import unittest
from typing import List


class Solution():
    def find_subsequence(self, t: List[str], output: List[str], idx: int, ans: List[str]) -> List[str]:
        if idx >= len(t):
            ans.append("".join(output))
            return

        else:
            element = t[idx]
            output.append(element)
            self.find_subsequence(t, output, idx + 1, ans)
            output.pop()
            self.find_subsequence(t, output, idx + 1, ans)
        return ans

    #TLE
    def isSubsequence(self, s: str, t: str) -> bool:
        t_arr = [ch for ch in t]
        subsequence = self.find_subsequence(t_arr, [], 0, [])
        if subsequence is None:
            if len(s) == 0:
                return True
            else:
                return False
        if s in subsequence:
            return True
        else:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.isSubsequence("abc","ahbgdc"))

    def test_case2(self):
        self.assertFalse(self.obj.isSubsequence("axc","ahbgdc"))

    def test_case3(self):
        self.assertTrue(self.obj.isSubsequence("",""))