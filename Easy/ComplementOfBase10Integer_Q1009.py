"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

    For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

Given an integer n, return its complement.



Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.



Constraints:

    0 <= n < 109



Note: This question is the same as 476: https://leetcode.com/problems/number-complement/

"""
import unittest


class Solution:
    def bitwiseComplement(self, n: int) -> int:

        mask = 0
        num = n
        count_of_ones = 0
        if n == 0:
            return 1
        while num != 0:
            num = num >> 1
            count_of_ones += 1
        while count_of_ones != 0:
            mask = mask << 1
            mask = mask | 1
            count_of_ones -= 1

        return (~n & mask)

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_edge_case(self):
        self.assertEqual(self.obj.bitwiseComplement(0),1)

    def test_case_1(self):
        self.assertEqual(self.obj.bitwiseComplement(5),2)

    def test_case_2(self):
        self.assertEqual(self.obj.bitwiseComplement(7),0)

    def test_case_3(self):
        self.assertEqual(self.obj.bitwiseComplement(10),5)
