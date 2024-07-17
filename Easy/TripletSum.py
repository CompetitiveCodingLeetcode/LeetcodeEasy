"""
educative question

find if a triplet exists such that their sum is equal to K. Given: i!=j,i!=k,j!=k.

two pointer approach
"""
import unittest


class Solution:
    def find_sum_of_three(self,nums, target):
        # Replace this placeholder return statement with your code
        nums = sorted(nums)
        for i in range(0, len(nums)):
            low = i + 1
            high = len(nums) - 1
            curr_sum = nums[i]
            while low < high and (low < len(nums)) and (high > i):
                if curr_sum + nums[low] + nums[high] == target:
                    return True
                elif curr_sum + nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1

        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertFalse(self.obj.find_sum_of_three([1,-1,0],-1))

    def test_case2(self):
        self.assertTrue(self.obj.find_sum_of_three([3,7,1,2,8,4,5] , 10))

    def test_case3(self):
        self.assertFalse(self.obj.find_sum_of_three([3,7,1,2,8,4,5] , 21))

    def test_case4(self):
        self.assertTrue(self.obj.find_sum_of_three([-1,2,1,-4,5,-3] , -8))

    def test_case5(self):
        self.assertTrue(self.obj.find_sum_of_three([-1,2,1,-4,5,-3] , 0))