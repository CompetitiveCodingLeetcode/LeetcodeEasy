"""
You are given an array Arr of size N. You have to find the K-th largest sum of contiguous subarray within the array elements. In other words, overall subarrays, find the subarray with kth largest sum and return its sum of elements.



Example 1:

Input:
N = 3
K = 2
Arr = {3,2,1}
Output:
5
Explanation:
The different subarray sums we can get from the array
are = {6,5,3,2,1}. Where 5 is the 2nd largest.


Example 2:

Input:
N = 4
K = 3
Arr = {2,6,4,1}
Output:
11
Explanation:
The different subarray sums we can get from the array
are = {13,12,11,10,8,6,5,4,2,1}. Where 11 is the 3rd largest.


Your Task:
You don't need to read input or print anything. Your task is to complete the function kthLargest() which takes the array Arr[] and its size N as inputs and returns the Kth largest subarray sum.



Expected Time Complexity: O(N2 * log K)
Expected Auxiliary Space: O(K)

https://www.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

"""
import unittest
from typing import List
from heapq import heappush,heappop

class Solution:
    def kthLargest(self, N: int, K: int, Arr: List[int]) -> int:
        # code here

        k_largest_sums = []
        for i in range(0, N):
            sub_arr = []
            sub_arr_sum = 0
            for j in range(i, N):
                sub_arr.append(Arr[j])
                sub_arr_sum += Arr[j]
                if len(k_largest_sums) < K:
                    heappush(k_largest_sums, sub_arr_sum)
                elif sub_arr_sum > k_largest_sums[0]:
                    heappop(k_largest_sums)
                    heappush(k_largest_sums, sub_arr_sum)

        return k_largest_sums[0]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.kthLargest(3,2,[3,2,1]),5)

    def test_case2(self):
        self.assertEqual(self.obj.kthLargest(4,3,[2,6,4,1]),11)