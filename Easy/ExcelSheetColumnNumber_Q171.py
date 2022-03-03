"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""
import unittest


class Solution:

    """
    Complexity Analysis

Time complexity : O(N) where NN is the number of characters in the input string.

Space complexity : O(1)
    """
    def titleToNumber(self, columnTitle: str) -> int:
        val = 0
        columnTitle_len = len(columnTitle)
        for column_title_char in columnTitle:
            multiplication_factor = pow(26, columnTitle_len - 1)
            val += ((ord(column_title_char) - ord('A') + 1) * multiplication_factor)
            columnTitle_len -= 1

        return val

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.titleToNumber("A"),1)

    def test_case2(self):
        self.assertEqual(self.obj.titleToNumber("AB"),28)

    def test_case3(self):
        self.assertEqual(self.obj.titleToNumber("ZY"),701)

