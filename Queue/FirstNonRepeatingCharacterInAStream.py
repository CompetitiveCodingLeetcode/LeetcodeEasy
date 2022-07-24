"""
Given a stream of characters and we have to find first non repeating character each time a character is inserted to the stream.
Input  : a a b c
Output : a -1 b b

Input  : a a c
Output : a -1 c

Approach:

"""
import unittest


class Solution():
    def find_non_repeating_character(self,s):
        char_count = [0]*26
        dq = []
        ans = []
        for ch in s:
            if ch in dq and ch == dq[0]:
                dq.pop(0)
            else:
                if char_count[ord(ch)-ord('a')] == 0:
                    char_count[ord(ch)-ord('a')] += 1
                    dq.append(ch)
                elif char_count[ord(ch)-ord('a')] > 0 and dq[-1] == ch:
                    dq.pop()
            if dq:
                ans.append(dq[0])
            else:
                ans.append(-1)

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.find_non_repeating_character("aabc"),['a',-1,'b','b'])

    def test_case2(self):
        self.assertListEqual(self.obj.find_non_repeating_character("aac"),['a',-1,'c'])

    def test_case3(self):
        self.assertListEqual(self.obj.find_non_repeating_character("geeksforgeeksandgeeksquizfor"),['g','g','g','g','g','g','g','g','k','k','k','s','f','f','f','f','f','f','f','f','f','f','f','f','f','o','r','a'])