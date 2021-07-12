"""
`Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true



Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.


"""

import unittest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        else:
            for i in range(s_len):
                if s[i] in mapping_s_t:
                    if mapping_s_t[s[i]] != t[i]:
                        return False
                if t[i] in mapping_t_s:
                    if mapping_t_s[t[i]] != s[i]:
                        return False
                else:
                    mapping_s_t[s[i]] = t[i]
                    mapping_t_s[t[i]] = s[i]
            return True


class TestSolution(unittest.TestCase):
    def test_success1(self):
        self.assertTrue(Solution().isIsomorphic("egg", "add"))

    def test_success2(self):
        self.assertTrue(Solution().isIsomorphic("paper", "title"))

    def test_failure1(self):
        self.assertFalse(Solution().isIsomorphic("foo", "bar"))

    def test_edge_case(self):
        self.assertFalse(Solution().isIsomorphic("badc", "baba"))


# Approach: maping from s to t and mapping from t to s is done simultaneously. Also if the char is not in mapping then add in dictionary else check if its value is not equal to other string's char then return False.