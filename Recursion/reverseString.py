"""
code to reverse a string recursively
"""
import unittest


def reverseString(s:str)->str:
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverseString(s[0:len(s)-1])


class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("",reverseString(""))

    def test_case2(self):
        self.assertEqual("a",reverseString("a"))

    def test_case3(self):
        self.assertEqual("rabbab",reverseString("babbar"))

