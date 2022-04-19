"""
return sum of given array recursively
"""
import unittest
from typing import List


class Solution:
    def find_sum(self, arr:List[int], size:int)-> int:
        if size == 0:
            return 0
        elif size == 1:
            return arr[0]
        else:
            return arr[0] + self.find_sum(arr[1:],size-1)



class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.find_sum([1,2,3],3),6)

    def test_case2(self):
        self.assertEqual(self.obj.find_sum([],0),0)

    def test_case3(self):
        self.assertEqual(self.obj.find_sum([1],1),1)

    def test_case4(self):
        self.assertEqual(self.obj.find_sum([6,6],2),12)