"""
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.



Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]


Constraints:

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
"""
import unittest
from typing import List


class Solution:
    def reverse_string(self, l: List[str], ptr1: int, ptr2: int) -> None:
        while ptr1 < ptr2:
            temp = l[ptr1]
            l[ptr1] = l[ptr2]
            l[ptr2] = temp

            ptr1 += 1
            ptr2 -= 1

    def reverse_each_word(self, l: List[str]) -> None:
        n = len(l)
        ptr1 = ptr2 = 0

        while ptr1 < n:
            while ptr2 < n and l[ptr2] != " ":
                ptr2 += 1
            self.reverse_string(l, ptr1, ptr2 - 1)
            ptr1 = ptr2 + 1
            ptr2 += 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        ptr1 = 0
        ptr2 = len(s) - 1

        # reverse  the entire string
        self.reverse_string(s, ptr1, ptr2)

        # reverse the words
        self.reverse_each_word(s)


