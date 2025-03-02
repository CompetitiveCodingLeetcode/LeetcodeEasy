"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.



Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.


Constraints:

n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
"""
import unittest
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height_list = []
        for i in range(0, len(names)):
            name_height_list.append([heights[i], names[i]])
        name_height_list = sorted(name_height_list, key=lambda x: x[0], reverse=True)
        idx = 0
        for height_name in name_height_list:
            heights[idx] = height_name[0]
            names[idx] = height_name[1]
            idx += 1
        return names

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.sortPeople(["Mary","John","Emma"],[180,165,170]),["Mary","Emma","John"])

    def test_case2(self):
        self.assertListEqual(self.obj.sortPeople(["Alice","Bob","Bob"],[155,185,150]),["Bob","Alice","Bob"])