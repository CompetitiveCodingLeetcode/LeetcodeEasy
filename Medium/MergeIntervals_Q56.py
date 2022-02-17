"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = []
        count = -1
        if len(intervals) == 1:
            return intervals
        for i in range(0, len(intervals)):
            if count == -1:
                if sorted_intervals[i][1] >= sorted_intervals[i + 1][0]:
                    temp = []
                    temp.append(min(sorted_intervals[i][0], sorted_intervals[i + 1][0]))
                    temp.append(max(sorted_intervals[i][1], sorted_intervals[i + 1][1]))
                    count += 1
                    merged_intervals.append(temp)
                else:
                    merged_intervals.append(sorted_intervals[i])
                    count += 1
            else:
                if merged_intervals[count][1] >= sorted_intervals[i][0]:
                    temp = []
                    temp.append(min(merged_intervals[count][0], sorted_intervals[i][0]))
                    temp.append(max(merged_intervals[count][1], sorted_intervals[i][1]))
                    if temp not in merged_intervals:
                        merged_intervals[count] = temp
                else:
                    merged_intervals.append(sorted_intervals[i])
                    count += 1

        return merged_intervals


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.merge([[1,3],[2,6],[8,10],[15,18]]),[[1,6],[8,10],[15,18]])

    def test_case2(self):
        self.assertEqual(self.obj.merge([[1,4],[4,5]]),[[1,5]])

    def test_case3(self):
        self.assertEqual(self.obj.merge([[0,4],[1,4]]),[[0,4]])

    def test_case4(self):
        self.assertEqual(self.obj.merge([[1,4],[0,1]]),[[0,4]])

    def test_case5(self):
        self.assertEqual(self.obj.merge([[1,4],[0,0]]),[[0,0],[1,4]])

    def test_case6(self):
        self.assertEqual(self.obj.merge([[1,4],[0,2],[3,5]]),[[0,5]])

    def test_case7(self):
        self.assertEqual(self.obj.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]),[[1,10]])

    def test_case8(self):
        self.assertEqual(self.obj.merge([[2,3],[5,5],[2,2],[3,1],[3,4],[3,4]]),[[2,4],[5,5]])