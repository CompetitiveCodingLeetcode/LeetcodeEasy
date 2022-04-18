"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


APPROACH: uses include and exclude calls
in include call - we include the ith element in output array and do recursive call
in exclude call - increment the value of i and do recursive call

base case : when i>=len(arr) : then add your output to ans
"""
import unittest
from typing import List


class Solution():
    def find_subsets(self,nums:List[int],output:List[int],index:int,ans:List[List[int]]):
        if index>=len(nums):
            if output not in ans:
                #TODO: need to check why output.copy() is used
                ans.append(output.copy())
            # output=[]
            print(ans)
            return

        else:

            #include call
            print("output=",output)
            element = nums[index]
            output.append(element)
            self.find_subsets(nums,output,index+1,ans)
            output.pop()
            # exclude call
            self.find_subsets(nums, output, index + 1, ans)
        return ans


    def subsets(self, nums: List[int]) -> List[List[int]]:
        index=0
        output=[]
        ans=[[]]
        self.find_subsets(nums,output,index,ans)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def is_present(self,actual,expected):
        for item in actual:
            if item not in expected:
                return False

        return True

    def test_case1(self):
        self.assertEqual(len(self.obj.subsets([1,2,3])),8)
        actual = self.obj.subsets([1,2,3])
        expected = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
        self.assertTrue(self.is_present(actual,expected))
