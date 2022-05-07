"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
import unittest
from typing import List


class Solution:
    def __init__(self, s:List[str]):
        self.s = s


    def reverseString(self) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1 = 0
        ptr2 = len(self.s) -1
        while ptr1<ptr2:
            temp = self.s[ptr1]
            self.s[ptr1] = self.s[ptr2]
            self.s[ptr2] = temp
            ptr1 += 1
            ptr2 -= 1

    def reverseStringUsingStack(self) -> str:
        ans = ""
        s_stack = []
        count = 0
        while count != len(self.s):
            s_stack.append(self.s[count])
            count += 1
        while len(s_stack) != 0:
            ans += s_stack.pop()
            print(s_stack)
        res = [ch for ch in ans]
        return res

class TestSolution(unittest.TestCase):

    def test_case1(self):
        self.obj = Solution(["h","e","l","l","o"])
        self.obj.reverseString()
        self.assertEqual(self.obj.s,["o","l","l","e","h"])

    def test_case2(self):
        self.obj = Solution(["H","a","n","n","a","h"])
        self.obj.reverseString()
        self.assertEqual(self.obj.s, ["h","a","n","n","a","H"])

    def test_case1_stack_approach(self):
        self.obj = Solution(["h","e","l","l","o"])
        self.assertEqual(self.obj.reverseStringUsingStack(),["o","l","l","e","h"])

    def test_case2_stack_approach(self):
        self.obj = Solution(["H","a","n","n","a","h"])
        self.assertEqual(self.obj.reverseStringUsingStack(),["h","a","n","n","a","H"])

