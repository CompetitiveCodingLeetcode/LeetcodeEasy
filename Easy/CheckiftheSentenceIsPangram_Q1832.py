"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
import unittest


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = {}
        for ch in sentence:
            if ch in alphabets.keys():
                alphabets[ch] += 1
            else:
                alphabets[ch] = 1

        for key, val in alphabets.items():
            if val == 0:
                return False

        if len(alphabets.keys()) != 26:
            return False

        return True

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

    def test_case2(self):
        self.assertFalse(self.obj.checkIfPangram("leetcode"))