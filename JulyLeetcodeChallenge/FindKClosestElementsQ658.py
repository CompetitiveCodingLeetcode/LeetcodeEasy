"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b



Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]



Constraints:

    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104


Edge cases:
1. [1,1,1,10,10,10]
    k=1
    x=9
"""

from typing import List


class Solution:
    def search_x(self, arr, x):
        low = 0
        arr_len = len(arr)
        high = arr_len - 1
        diff = 300
        while low <= high:
            mid = int((low + high) / 2)
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                if (arr[mid] - x) < diff:  # here
                    diff = arr[mid] - x
                    pos = mid
                high = mid - 1
            else:
                if (x - arr[mid]) < diff:
                    diff = x - arr[mid]
                    pos = mid
                low = mid + 1
        return pos

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos_x = self.search_x(arr, x)
        min_list = []
        for i in range(k):
            b_index = pos_x - k + 1 + i
            e_index = pos_x + 1 + i

            if pos_x + 1 >= k:
                if e_index > len(arr):
                    break
                ans_list = arr[b_index:e_index]
            else:
                b_index += (k - pos_x) - 1
                e_index += (k - pos_x) - 1
                if e_index > len(arr):
                    break
                ans_list = arr[b_index:e_index]
            if i == 0:
                diff = 0
                for j in range(e_index - b_index):
                    diff += abs(ans_list[j] - x)
            else:
                diff = diff + abs(ans_list[-1] - x)
            min_list.append((diff, b_index))
            diff = diff - (abs(ans_list[0] - x))
        if not min_list:
            return arr[b_index:e_index]
        temp = min(min_list)
        return arr[temp[1]:temp[1] + k]


obj = Solution()
print(obj.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))
print(obj.findClosestElements([1], 1, 1))
print(obj.findClosestElements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], 4, 5))
print(obj.findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9))
print(obj.findClosestElements([1, 2, 3, 3, 6, 6, 7, 7, 9, 9], 8, 8))
print(obj.findClosestElements([1, 3], 1, 2))
print(obj.findClosestElements([1, 2, 3, 3, 3, 5, 6, 6, 7], 4, 4))
print(obj.findClosestElements(
    [0, 0, 1, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9, 11, 12, 13, 14, 14, 15, 16, 19, 19, 20, 22, 24, 25, 25, 25, 27, 27, 28, 33,
     34, 34, 34, 37, 38, 38, 40, 40, 41, 41, 42, 44, 45, 46, 47, 50, 51, 52, 53, 53, 56, 56, 60, 61, 62, 64, 64, 64, 64,
     65, 65, 66, 67, 68, 68, 68, 72, 73, 73, 74, 75, 75, 76, 78, 79, 80, 80, 80, 81, 81, 82, 83, 84, 85, 87, 88, 88, 89,
     89, 91, 92, 94, 96, 96, 96, 96, 97, 99], 94, 69))
