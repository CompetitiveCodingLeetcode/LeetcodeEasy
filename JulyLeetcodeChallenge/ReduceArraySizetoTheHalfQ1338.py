"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.



Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.

Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Example 3:

Input: arr = [1,9]
Output: 1

Example 4:

Input: arr = [1000,1000,3,7]
Output: 1

Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5



Constraints:

    1 <= arr.length <= 10^5
    arr.length is even.
    1 <= arr[i] <= 10^5

"""
import collections
from typing import List
import unittest
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_len = len(arr)
        c = collections.Counter(arr)
        c = sorted(c.values())

        count = 0
        size = 0

        while count < arr_len / 2:
            size += 1
            v = c.pop()
            count += v
        return size
        # for i in range(arr_len):
        #     if arr[i] in arr_elements_count:
        #         arr_elements_count[arr[i]] += 1
        #     else:
        #         arr_elements_count[arr[i]] = 1
        #
        # sorted_arr_elements_count = dict(sorted(arr_elements_count.items(), key=lambda x: x[1], reverse=True))
        # min_set_size = 0
        # count_sum = 0
        # for i in sorted_arr_elements_count.items():
        #     count_sum += i[1]
        #     min_set_size += 1
        #     if count_sum >= arr_len / 2:
        #         break
        # return min_set_size


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_success1(self):
        self.assertEqual(2, self.obj.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))

    def test_success2(self):
        self.assertEqual(1, self.obj.minSetSize([7, 7, 7, 7, 7, 7]))

    def test_success3(self):
        self.assertEqual(1, self.obj.minSetSize([1, 9]))

    def test_success4(self):
        self.assertEqual(1, self.obj.minSetSize([1000, 1000, 3, 7]))

    def test_success5(self):
        self.assertEqual(5, self.obj.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
