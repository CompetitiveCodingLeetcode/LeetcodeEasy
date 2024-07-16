"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
import unittest


class Solution:
    def isInvalid(self, temp):
        char_freq = {}
        for c in temp:
            if c in char_freq.keys():
                return True
            else:
                char_freq[c] = 1
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        if len(s) == 1:
            return 1
        for r in range(0, len(s) + 1):
            temp = s[l:r]
            if temp:
                while self.isInvalid(temp):
                    l += 1
                    temp = s[l:r]
            max_len = max(max_len, r - l)
        return max_len


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.lengthOfLongestSubstring("abcabcbb"),3)

    def test_case2(self):
        self.assertEqual(self.obj.lengthOfLongestSubstring("bbbbb"),1)

    def test_case3(self):
        self.assertEqual(self.obj.lengthOfLongestSubstring("pwwkew"),3)

    def test_case4(self):
        self.assertEqual(self.obj.lengthOfLongestSubstring(" "),1)

    def test_case5(self):
        self.assertEqual(self.obj.lengthOfLongestSubstring("au"),2)