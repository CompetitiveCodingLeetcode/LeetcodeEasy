"""
recursive solution to find a^b
"""
import unittest


def find_power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*find_power(a,b-1)


def find_power_approach2(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    ans = find_power_approach2(a,b//2)

    if b%2 == 0:
        return ans*ans
    else:
        return a*ans*ans




class Solution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(1,find_power(3,0))

    def test_case2(self):
        self.assertEqual(3,find_power(3,1))

    def test_case3(self):
        self.assertEqual(9,find_power(3,2))

    def test_case1_approach2(self):
        self.assertEqual(1,find_power_approach2(3,0))

    def test_case2_approach2(self):
        self.assertEqual(3,find_power_approach2(3,1))

    def test_case3_approach2(self):
        self.assertEqual(9,find_power_approach2(3,2))