import unittest
from typing import List

# Time complexity=O(n^2)
def find_max_product_bruteforce_approach(nums: List[int]) -> int:
    max_product = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] > max_product:
                max_product = nums[i] * nums[j]

    return max_product

# time complexity=O(nlogn)
def find_max_product_sort_approach(nums: List[int]) -> int:
    nums.sort()
    max_product = nums[0] * nums[1]

    # handling the product of 2 negative integers if greater than the max_product as the negative numbers while sorting will come in the end of array
    if nums[len(nums) - 1] * nums[len(nums) - 2] > max_product:
        max_product = nums[len(nums) - 1] * nums[len(nums) - 2]
    return max_product


class TestSolution(unittest.TestCase):
    def test_all_positive_elements(self):
        self.assertEqual(40, find_max_product_bruteforce_approach([1, 2, 8, 3, 5]))

    def test_negative_elements(self):
        self.assertEqual(40, find_max_product_bruteforce_approach([1, 2, -8, -3, -5]))

    def test_sort_approach_all_positive_elements(self):
        self.assertEqual(40, find_max_product_sort_approach([1, 2, 8, 3, 5]))

    def test_sort_approach_negative_elements(self):
        self.assertEqual(40, find_max_product_sort_approach([1, 2, -8, -3, -5]))

