"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_char_idx = {}
        idx = 0
        for s_char in s:
            if s_char in s_char_idx.keys():
                s_char_idx[s_char].append(idx)
                idx += 1
            else:
                s_char_idx[s_char] = [idx]
                idx += 1

        non_repeating_idx = -1
        for key, val in s_char_idx.items():
            if len(val) == 1:
                if non_repeating_idx == -1:
                    non_repeating_idx = val[0]
                elif non_repeating_idx != -1 and val[0] < non_repeating_idx:
                    non_repeating_idx = val[0]

        return non_repeating_idx


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.firstUniqChar("leetcode"),0)

    def test_case2(self):
        self.assertEqual(self.obj.firstUniqChar("loveleetcode"),2)

    def test_case3(self):
        self.assertEqual(self.obj.firstUniqChar("aabb"),-1)