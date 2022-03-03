"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""
import unittest
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        sorted_intervals_len = len(sorted_intervals)
        for i in range(0, sorted_intervals_len - 1):
            if sorted_intervals[i + 1][0] < sorted_intervals[i][1]:
                return False
        return True

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.canAttendMeetings([[7,10],[2,4]]))

    def test_case2(self):
        self.assertFalse(self.obj.canAttendMeetings([[0,30],[5,10],[15,20]]))
