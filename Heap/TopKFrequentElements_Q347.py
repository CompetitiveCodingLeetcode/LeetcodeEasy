"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Time complexity: O(klogD + DlogD) ; D=number of distinct integers
"""
import unittest
from heapq import heappush, heappop
from typing import List

class NumFreq:
    def __init__(self, num, freq):
        self.number = num
        self.freq = freq

    def __lt__(self, nxt):
        return self.freq < nxt.freq

    def __gt__(self, nxt):
        return self.freq > nxt.freq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            if num in num_freq.keys():
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        num_freq_l = [[k, v] for k, v in num_freq.items()]

        k_freq_num = []

        for i in range(0, k):
            heappush(k_freq_num, NumFreq(num_freq_l[i][0], num_freq_l[i][1]))

        for i in range(k, len(num_freq_l)):
            if NumFreq(num_freq_l[i][0], num_freq_l[i][1]) > k_freq_num[0]:
                heappop(k_freq_num)
                heappush(k_freq_num, NumFreq(num_freq_l[i][0], num_freq_l[i][1]))
        ans = []
        for i in range(0, len(k_freq_num)):
            ans.append(k_freq_num[i].number)

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(sorted(self.obj.topKFrequent([1,1,1,2,2,3],2)),[1,2])

    def test_case_2(self):
        self.assertEqual(sorted(self.obj.topKFrequent([1],1)),[1])