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


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count_chars = [0] * 26
        len_s1 = len(s1)
        len_s2 = len(s2)
        ctrl_flag = True

        for ch in s1:
            count_chars[ord(ch) - ord('a')] += 1

        for i in range(0, len_s2 - len_s1):
            window = s2[i:i + len_s1]
            ctrl_flag = True

            for ch in window:
                if ch not in s1:
                    ctrl_flag = False

            if ctrl_flag:
                for ch in window:
                    count_chars[ord(ch) - ord('a')] -= 1

        for i in range(0, 26):
            if count_chars[i] != 0:
                return False
        return True

