"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
import unittest
from typing import List


class Solution():
    def find_letter_combinations(self, digits, output, idx, ans, mapping) -> List[str]:
        if idx >= len(digits):
            ans.append("".join(output))
            return
        else:
            element = ord(digits[idx]) - ord('0')
            value = mapping[element]
            for i in range(0, len(value)):
                output.append(value[i])
                self.find_letter_combinations(digits, output, idx + 1, ans, mapping)
                output.pop()
            return ans

    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        ans = []
        if len(digits) == 0:
            return []
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = self.find_letter_combinations(digits, output, 0, ans, mapping)
        return res


class TestSoution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.letterCombinations("23"),["ad","ae","af","bd","be","bf","cd","ce","cf"])

    def test_case2(self):
        self.assertEqual(self.obj.letterCombinations(""),[])

    def test_case3(self):
        self.assertEqual(self.obj.letterCombinations("2"),["a","b","c"])