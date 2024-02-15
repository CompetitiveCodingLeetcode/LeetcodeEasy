"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


Approach 1:
sort the array in descending order and the element at kth position in sorted array is the answer.
Time complexity: O(nlogn)
Space complexity: O(1)

Approach 2:
1. create min heap for first k elements of array
2. for elemnts from k to len-1
    i) if the element is greater than root of heap then delete/pop elemnt from heap and put the greater element
3. return root of min heap
Time complexity: O(k +(n-k)logk)
Space complexity: O(k)

"""
import unittest
from typing import List
from heapq import heappush,heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        for i in range(0,k):
            heappush(min_heap,nums[i])

        for i in range(k,len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap,nums[i])

        return min_heap[0]

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
    def test_case_one(self):
        self.assertEqual(self.obj.findKthLargest([3,2,1,5,6,4],2),5)

    def test_case_two(self):
        self.assertEqual(self.obj.findKthLargest([3,2,3,1,2,4,5,5,6],4),4)
