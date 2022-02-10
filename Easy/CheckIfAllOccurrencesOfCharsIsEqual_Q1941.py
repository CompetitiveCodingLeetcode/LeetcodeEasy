"""

Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).



Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
import unittest
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_dict = Counter(s)
        count = s_dict[s[0]]
        for key,val in s_dict.items():
            if val != count:
                return False
        return True

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.areOccurrencesEqual("abacbc"))

    def test_case2(self):
        self.assertFalse(self.obj.areOccurrencesEqual("aaabb"))