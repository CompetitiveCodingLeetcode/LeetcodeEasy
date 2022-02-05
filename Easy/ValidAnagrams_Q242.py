"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""
import unittest


class Solution:
    #O(n) - 3 pass
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        if len(s) != len(t):
            return False
        for chars_s in s:
            if chars_s in s_dict.keys():
                s_dict[chars_s] += 1
            else:
                s_dict[chars_s] = 1
        for chars_t in t:
            if chars_t not in s_dict.keys():
                return False
            else:
                if s_dict[chars_t] == 0:
                    return False
                s_dict[chars_t] -= 1

        for s_char, s_char_count in s_dict.items():
            if s_char_count != 0:
                return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1_approach1(self):
        self.assertTrue(self.obj.isAnagram("anagram","nagaram"))

    def test_case2_approach1(self):
        self.assertFalse(self.obj.isAnagram("rat","car"))

