"""Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.For example, 121 is palindrome while 123 is not.
Example
1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads - 121. From right to left, it becomes 121 -.Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads
01
from right to

left.Therefore
it is not a
palindrome.

Example
4:

Input: x = -101
Output: false

Constraints:

-231 <= x <= 231 - 1"""
import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            num=x
            rev=0
            while num!=0:
                d=num%10
                # //----> It returns floor value for both integer and floating point arguments
                num=num//10
                rev=rev*10+d
            if rev==x:
                return True
            else:
                return False

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertFalse(self.obj.isPalindrome(-121))

    def test_case2(self):
        self.assertFalse(self.obj.isPalindrome(123))

    def test_case3(self):
        self.assertTrue(self.obj.isPalindrome(121))
