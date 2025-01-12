"""

Given a string, return true if it is a valid pallindrome else false

Example 1: abc
output: false

Example 2: abba
output: true

Time Complexity: O(n)
Space Complexity: O(1)
"""
import unittest

class ValidPallindrome:
    def isValid(self,s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start<=end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

class TestValidPallindrome(unittest.TestCase):
    def setUp(self):
        self.obj = ValidPallindrome()
    def test_case_1(self):
        self.assertTrue(self.obj.isValid("aba"))

    def test_case_2(self):
        self.assertFalse(self.obj.isValid("abc"))

    def test_case_3(self):
        self.assertTrue(self.obj.isValid("a"))

    def test_case_4(self):
        self.assertTrue(self.obj.isValid(""))