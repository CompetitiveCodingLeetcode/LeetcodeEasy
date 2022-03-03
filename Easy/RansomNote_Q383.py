"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

"""
import collections
import unittest


class Solution:

    # using two hashmaps
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomeNote_chars = {}
        magazine_chars = {}

        for rn_char in ransomNote:
            if rn_char in ransomeNote_chars.keys():
                ransomeNote_chars[rn_char] += 1
            else:
                ransomeNote_chars[rn_char] = 1

        for m_char in magazine:
            if m_char in magazine_chars.keys():
                magazine_chars[m_char] += 1
            else:
                magazine_chars[m_char] = 1

        for key, val in ransomeNote_chars.items():
            if key not in magazine_chars.keys():
                return False
            if magazine_chars[key] < val:
                return False
        return True


    # using one hash map
    def canConstruct_approach2(self, ransomNote: str, magazine: str) -> bool:
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        letters = collections.Counter(magazine)

        # For each character, c, in the ransom note:
        for c in ransomNote:
            # If there are none of c left, return False.
            if letters[c] <= 0:
                return False
            # Remove one of c from the Counter.
            letters[c] -= 1
        # If we got this far, we can successfully build the note.
        return True

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertFalse(self.obj.canConstruct("a","b"))

    def test_case2(self):
        self.assertTrue(self.obj.canConstruct("aa","aab"))

    def test_case3(self):
        self.assertFalse(self.obj.canConstruct("aa","ab"))

    def test_case1_approach2(self):
        self.assertFalse(self.obj.canConstruct_approach2("a","b"))

    def test_case2_approach2(self):
        self.assertTrue(self.obj.canConstruct_approach2("aa","aab"))

    def test_case3_approach2(self):
        self.assertFalse(self.obj.canConstruct_approach2("aa","ab"))