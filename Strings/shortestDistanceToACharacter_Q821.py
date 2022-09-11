"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.



Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]


Constraints:

1 <= s.length <= 104
s[i] and c are lowercase English letters.
It is guaranteed that c occurs at least once in s.


TODO:
Understand the following approach for two pointers and one pass:
The idea is that every character is within a closed interval, with at least 1 sitting on an index where it is mapped to the target character. For example

"leetcode", "e"
When you are on the first character, the right pointer is 1, left pointer should be None
What if you are on 3? the "t"? Well, you are surrounded by "e" on both left and right, look at 2 and 7

My very first approach is for every character, get the closest "e" on my right. There are 2 problems

How about the one on your left?
Handling an array is just as troublesome
Besides, you don't need a ton of indexes sitting idly. You can get the closest "e" on the right on demand
This problem is not difficult. It is not difficult on a scale like suffix tree on Ukkonen's construction. But it is difficult in another way, like in a binary search way of difficult. To name a few,

What should be the initial value for afterc and beforec?
What should be the condition for which the "finding_right" function predicate on?
All of which are not difficult per se apart from warranting a lot, like fr a lot, of visualization.
I literally forgot afterc += 1 until I put down the log.
The mark that I missed may not be the one you missed. So I will just paste the code and, most importantly, the information I deem cruical and necessary for clarity in the following.

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        afterc = -1
        beforec = -1
        i = 0
        ans = []
        while i < len(s):
            print(s)
            print(s[:i])
            if afterc < i:
                beforec = afterc
                afterc += 1
                print(f"Need adjust: afterc < i: {afterc} < {i}")
                while afterc < len(s) and s[afterc] != c:
                    afterc += 1
                print(f"After adjust: {afterc}")
            if beforec == -1:
                print(f"beforec == -1")
                print(f"ans.append({afterc - i})")
                ans.append(afterc - i)
            elif afterc == len(s):
                print(f"afterc == len(s)")
                print(f"ans.append({i - beforec})")
                ans.append(i - beforec)
            else:
                print(f"else")
                print(f"afterc - i: {afterc - i}, i - beforec: {i - beforec}, ans.append({min(afterc - i, i - beforec)})")
                ans.append(min(afterc - i, i - beforec))
            i += 1
            print()
        return ans
Last but not least, the runtime is definitely O(n). There are only plenty of variables, afterc, beforec and i that could impact the run time. None of which would run more than O(n) for the entire program. The space is definitely O(1). So it is pretty good if I do say so myself.

"""
import unittest
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_indexes = []
        i = 0
        ans = []
        for ch in s:
            if ch == c:
                c_indexes.append(i)
            i += 1

        for i in range(0, len(s)):
            min_distance = len(s) + 1
            for idx in c_indexes:
                diff = abs(idx - i)
                if diff < min_distance:
                    min_distance = diff
            ans.append(min_distance)

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.shortestToChar("loveleetcode","e"),[3,2,1,0,1,0,0,1,2,2,1,0])

    def test_case2(self):
        self.assertListEqual(self.obj.shortestToChar("aaab","b"),[3,2,1,0])