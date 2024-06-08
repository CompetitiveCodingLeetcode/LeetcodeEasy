"""
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.



Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.


Constraints:

n == s.length
2 <= n <= 106
n is even.
s[i] is either '[' or ']'.
The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.

Approach written in Stack/minimumRemovesOrSwaps/MiimumCostToMakeStringVallid.py
"""
import unittest


class Solution:
    def minSwaps(self, s: str) -> int:
        opening_brackets = 0
        closing_brackets = 0
        stack = []

        for c in s:
            if c == '[':
                stack.append('[')
                opening_brackets += 1
            else:
                if len(stack) != 0:
                    stack.pop()
                    opening_brackets -= 1
                else:
                    closing_brackets += 1

        return (closing_brackets + 1) // 2

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.minSwaps("][]["),1)

    def test_case2(self):
        self.assertEqual(self.obj.minSwaps("]]][[["),2)

    def test_case3(self):
        self.assertEqual(self.obj.minSwaps("[]"),0)
