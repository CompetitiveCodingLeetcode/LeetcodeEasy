"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""
import unittest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1) - 1
        len2 = len(num2) - 1

        res = 0
        carry = 0
        ans = ""
        while len1 >= 0 and len2 >= 0:
            d1 = ord(num1[len1]) - 48  # 5
            d2 = ord(num2[len2]) - 48  # 7
            len1 -= 1  # 0
            len2 -= 1  # -1

            res = d1 + d2 + carry  # 13
            if res > 9:
                carry = res // 10  # 1
                res = res % 10  # 3
            else:
                carry = 0
            ans = str(res) + ans  # 33

        while len1 >= 0:
            d1 = ord(num1[len1]) - 48
            len1 -= 1

            res = d1 + carry

            if res > 9:
                carry = res // 10
                res = res % 10
            else:
                carry = 0
            ans = str(res) + ans

        while len2 >= 0:
            d2 = ord(num2[len2]) - 48
            len2 -= 1

            res = d2 + carry

            if res > 9:
                carry = res // 10
                res = res % 10
            else:
                carry = 0
            ans = str(res) + ans
        if carry > 0:
            ans = str(carry) + ans
        return ans

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.addStrings("11","123"),"134")

    def test_case2(self):
        self.assertEqual(self.obj.addStrings("456","77"),"533")

    def test_case3(self):
        self.assertEqual(self.obj.addStrings("9","1"),"10")

    def test_case4(self):
        self.assertEqual(self.obj.addStrings("0","0"),"0")