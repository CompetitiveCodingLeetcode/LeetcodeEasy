"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: ""doG gniD""


Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        new_words=[]
        for word in words:
            word = word[::-1]
            new_words.append(word)
        s = " ".join(new_words)
        return s

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.reverseWords("Let's take LeetCode contest"),"s'teL ekat edoCteeL tsetnoc")

    def test_case2(self):
        self.assertEqual(self.obj.reverseWords("God Ding"),"doG gniD")

