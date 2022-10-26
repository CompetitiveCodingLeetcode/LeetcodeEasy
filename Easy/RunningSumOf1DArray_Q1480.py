"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

APPROACH:
Approach 1: Using Separate Space
Intuition

We are required to find the running sum of numbers nums[i] in the input array where i ranges from 0 to n-1 and n is the size of the input array. We can see that the running sum is the sum of all of the elements from index 0 to index i inclusive. Since we start building our output array at index 0, at each index i we have already calculated the sum of all numbers up to and including index i-1. Thus, instead of recalculating the sum, we can get the result for index i by simply adding the element at index i to the previously calculated running sum for index i-1.

Algorithm

Define an array result.
Initialize the first element of result with the first element of the input array.
At index i append the sum of the element nums[i] and previous running sum result[i - 1] to the result array.
We repeat step 3 for all indices from 1 to n-1.
Complexity Analysis

Time complexity: O(n) where nn is the length of the input array. This is because we use a single loop that iterates over the entire array to calculate the running sum.

Space complexity: O(1) since we don't use any additional space to find the running sum. Note that we do not take into consideration the space occupied by the output array.


Approach 2: Using Input Array for Output
Intuition

In the previous approach we created an extra array to store our results. However, we do not actually need to do so. We can obtain the same result without using extra space by performing the same operations on the input array instead.

Algorithm

Increase nums[i] by the previous index's running sum. The previous index's running sum is stored at index i-1 in the input array.
We repeat step 1 for all indices from 1 to n-1.
Complexity Analysis

Time complexity: O(n) where nn is the length of input array.

Space complexity: O(1) since we don't use any additional space to find the running sum. Note that we do not take into consideration the space occupied by the output array.


"""
import unittest
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        i = 0
        for num in nums:
            prefix_sum += nums[i]
            nums[i] = prefix_sum
            i += 1
        return nums

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.runningSum([1,2,3,4]),[1,3,6,10])

    def test_case2(self):
        self.assertEqual(self.obj.runningSum([1,1,1,1,1]),[1,2,3,4,5])

    def test_case3(self):
        self.assertEqual(self.obj.runningSum([3,1,2,10,1]),[3,4,6,16,17])