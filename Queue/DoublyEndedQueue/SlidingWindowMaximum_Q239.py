"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length


Approach:
1. Create a deque to store k elements.
2. Run a loop and insert first k elements in the deque. Before inserting the element, check if the element at the back of the queue is smaller than the current element, if it is so remove the element from the back of the deque, until all elements left in the deque are greater than the current element. Then insert the current element, at the back of the deque.
3. Now, run a loop from k to end of the array.
4. Print the front element of the deque.
5. Remove the element from the front of the queue if they are out of the current window.
6. Insert the next element in the deque. Before inserting the element, check if the element at the back of the queue is smaller than the current element, if it is so remove the element from the back of the deque, until all elements left in the deque are greater than the current element. Then insert the current element, at the back of the deque.
7. Print the maximum element of the last window.
"""
import unittest
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        ans = []
        # first window processing
        for i in range(0, k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        # update ans
        if dq:
            ans.append(nums[dq[0]])

        # process for other values
        for i in range(k, n):
            count = 0
            # removal
            while dq and (i - dq[0] >= k):
                dq.popleft()

            # addition
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            # update ans
            if dq:
                ans.append(nums[dq[0]])

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3),[3,3,5,5,6,7])

    def test_case2(self):
        self.assertListEqual(self.obj.maxSlidingWindow([1],1),[1])

    def test_case3(self):
        self.assertListEqual(self.obj.maxSlidingWindow([-1,1],1),[-1,1])

    def test_case4(self):
        self.assertListEqual(self.obj.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6],5),[10,10,9,2])