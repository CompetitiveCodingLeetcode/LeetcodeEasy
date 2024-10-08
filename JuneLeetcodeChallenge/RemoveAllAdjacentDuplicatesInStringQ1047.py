"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"



Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.


"""
import unittest


class Solution:
    def removeDuplicates(self, s: str) -> str:
        s_len = len(s)
        if s_len == 1:
            return s
        else:
            s_ind = 0
            e_ind = 1
            while len(s) and s_ind != e_ind:
                if s[s_ind] == s[e_ind]:
                    if e_ind == len(s) - 1:
                        temp = s[0:s_ind]
                    else:
                        temp = s[0:s_ind] + s[e_ind + 1:]
                    s = temp
                    if len(s) == 1:
                        break
                    if s_ind != 0:
                        s_ind = s_ind - 1
                        e_ind = s_ind + 1
                    else:
                        s_ind = 0
                        e_ind = s_ind + 1
                else:
                    s_ind = e_ind
                    if e_ind != len(s) - 1:
                        e_ind += 1
                if e_ind == len(s):
                    break
            return s

    def removeDuplicatesStackApproach(self, s):
        ans = ""
        for i in range(len(s)):
            if ans == "" or ans[-1] != s[i]:
                ans += s[i]
            else:
                ans = ans[:-1]
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("abbaca"),"ca")

    def test_case2(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("azxxzy"),"ay")

    def test_case3(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("aa"),"")

    def test_case4(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("a"),"a")

    def test_case5(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("aaaaaaaa"),"")

    def test_case6(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("aab"),"b")

    def test_case7(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("aabc"),"bc")

    def test_case8(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("baa"),"b")

    def test_case8(self):
        self.assertEqual(self.obj.removeDuplicatesStackApproach("bcaa"),"bc")
