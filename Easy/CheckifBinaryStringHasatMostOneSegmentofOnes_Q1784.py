"""
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.



Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true


Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '
"""
import unittest


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = 0
        for i in s:
            if i =='1' and flag == 0:
                flag = 1
            elif i =='0' and flag == 1:
                flag = 2
            elif i =='1' and flag == 2:
                return False
        return True

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.checkOnesSegment("10"))

    def test_case2(self):
        self.assertTrue(self.obj.checkOnesSegment("1"))

    def test_case3(self):
        self.assertFalse(self.obj.checkOnesSegment("1001"))

    def test_case4(self):
        self.assertTrue(self.obj.checkOnesSegment("110"))