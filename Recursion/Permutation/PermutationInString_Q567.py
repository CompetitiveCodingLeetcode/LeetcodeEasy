"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
import unittest


class Solution:
    def swap(self, s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

    def find_permutations(self, s, idx, ans):
        if idx >= len(s):
            ans.append("".join(s))
            return
        else:
            for i in range(idx, len(s)):
                self.swap(s, i, idx)
                self.find_permutations(s, idx + 1, ans)
                self.swap(s, i, idx)

    #output limit exceeded for : "algorithm","altruistic"
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = []
        s1_list = [ch for ch in s1]
        self.find_permutations(s1_list, 0, ans)

        for item in ans:
            if item in s2:
                return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.checkInclusion("ab","eidbaooo"))

    def test_case2(self):
        self.assertFalse(self.obj.checkInclusion("ab","eidboooo"))