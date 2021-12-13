"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:

Input: s = "triplepillooooow"
Output: 5

Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:

Input: s = "tourist"
Output: 1



Constraints:

    1 <= s.length <= 500
    s consists of only lowercase English letters.


"""
import unittest


class Solution:
    def maxPower(self, s: str) -> int:
            count = 0
            max_count = 0
            previous = None
            for c in s:
                if c == previous:
                    # if same as previous one, increase the count
                    count += 1
                else:
                    # else, reset the count
                    previous = c
                    count = 1
                max_count = max(max_count, count)
            return max_count

class  TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj=Solution()

    def test_count1(self):
        self.assertEqual(self.obj.maxPower("tourist"),1)

    def test_count2(self):
        self.assertEqual(self.obj.maxPower("cc"),2)

    def test_count3(self):
        self.assertEqual(self.obj.maxPower("abbcccddddeeeeedbca"),5)

    def test_count4(self):
        self.assertEqual(self.obj.maxPower("hooraaaaaaaaaaay"),11)

    def test_count5(self):
        self.assertEqual(self.obj.maxPower("leetcode"),2)
