"""
educative question

find if a triplet exists such that their sum is equal to K. Given: i!=j,i!=k,j!=k.

two pointer approach
First, sort the array in ascending order. To find a triplet whose sum is equal to the target value, loop through the entire array. In each iteration:

Store the current array element and set up two pointers (low and high) to find the other two elements that complete the required triplet.

The low pointer is set to the current loop’s index + 1.

The high is set to the last index of the array.

Calculate the sum of array elements pointed to by the current loop’s index and the low and high pointers.

If the sum is equal to target, return TRUE.

If the sum is less than target, move the low pointer forward.

If the sum is greater than target, move the high pointer backward.

Repeat until the loop has processed the entire array. If, after processing the entire array, we don’t find any triplet that matches our requirement, we return FALSE.

Time complexity
In the solution above, sorting the array takes
O(nlog(n)) and the nested loop takes
O(n^2)
 to find the triplet. Here, n is the number of elements in the input array. Therefore, the total time complexity of this solution is
O(nlogn+n^2), which simplifies to O(n^2)

Space complexity
Because we use the built-in Python function, sort(), so the space complexity of the provided solution is
O(n)
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