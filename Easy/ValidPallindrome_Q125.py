"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2:
            while ptr1 < ptr2 and not s[ptr1].isalnum():
                ptr1 += 1
            while ptr1 < ptr2 and not s[ptr2].isalnum():
                ptr2 -= 1

            if s[ptr1].lower() != s[ptr2].lower():
                return False

            ptr1 += 1
            ptr2 -= 1

        return True

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.isPalindrome("A man, a plan, a canal: Panama"))

    def test_case2(self):
        self.assertFalse(self.obj.isPalindrome("race a car"))

    def test_case3(self):
        self.assertTrue(self.obj.isPalindrome(" "))