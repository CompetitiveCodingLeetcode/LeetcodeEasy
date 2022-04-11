import time
import unittest
from typing import List


class Solution:
    def LinearSearch(self,nums: List[int], value: int) -> int:
        # start = time.time()

        for num in nums:
            if num == value:
                return nums.index(value)

    # enumerate approach
    # for idx, num in enumerate(nums):
    #     if num == value:
    #         pos = idx
    #         break
    #     end = time.time()
    #     print("time taken =", end - start)
        # time taken = 3.5762786865234375e-06 for index() approach
        # time taken = 5.9604644775390625e-06 for enumerate() approach
        return -1

    def linear_search_recursive(self, nums: List[int], size: int, target: int)-> bool:
        if size == 0:
            return False
        if nums[0] == target:
            return True
        else:
            return self.linear_search_recursive(nums[1:],size-1,target)



class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.linear_search_recursive([1,2,3,4],4,4))

    def test_case2(self):
        self.assertFalse(self.obj.linear_search_recursive([1,2,3,4],4,10))

    def test_case3(self):
        self.assertEqual(self.obj.LinearSearch([1,2,3,4],4),3)

    def test_case4(self):
        self.assertEqual(self.obj.LinearSearch([1,2,3,4],5),-1)
