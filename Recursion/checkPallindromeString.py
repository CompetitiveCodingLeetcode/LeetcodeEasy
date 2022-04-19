"""
check if string is pallindrome or not
"""
import unittest


def check_pallindrome(s:str,i:int,j:int)-> bool:
    if i>j:
        return True
    if s[i] == s[j]:
        return check_pallindrome(s,i+1,j-1)
    else:
        return False

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(check_pallindrome("aabbaa",0,len("aabbaa")-1))

    def test_case2(self):
        self.assertFalse(check_pallindrome("abc",0,len("abc")-1))
            