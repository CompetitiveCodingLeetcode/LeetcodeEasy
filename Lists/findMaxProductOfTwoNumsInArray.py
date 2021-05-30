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


# time complexity = O(n)
def find_max_product_optimized_approach(nums: List[int]) -> int:
    max_product_num1 = nums[0]
    max_product_num2 = 0

    min_product_num1 = nums[0]
    min_product_num2 = -1

    #if you start with  0 then last test case would fail
    for i in range(1, len(nums)):
        if nums[i] > max_product_num1:
            max_product_num2 = max_product_num1
            max_product_num1 = nums[i]
        elif nums[i] > max_product_num2:
            max_product_num2 = nums[i]

        if nums[i] < 0 and abs(nums[i]) > abs(min_product_num1):
            min_product_num2 = min_product_num1
            min_product_num1 = nums[i]
        elif nums[i] < 0 and abs(nums[i]) > abs(min_product_num2):
            min_product_num2 = nums[i]

    if min_product_num1 * min_product_num2 > max_product_num2 * max_product_num1:
        return min_product_num1 * min_product_num2
    else:
        return max_product_num2 * max_product_num1


class TestSolution(unittest.TestCase):
    def test_all_positive_elements(self):
        self.assertEqual(40, find_max_product_bruteforce_approach([1, 2, 8, 3, 5]))

    def test_negative_elements(self):
        self.assertEqual(40, find_max_product_bruteforce_approach([1, 2, -8, -3, -5]))

    def test_sort_approach_all_positive_elements(self):
        self.assertEqual(40, find_max_product_sort_approach([1, 2, 8, 3, 5]))

    def test_sort_approach_negative_elements(self):
        self.assertEqual(40, find_max_product_sort_approach([1, 2, -8, -3, -5]))

    def test_optimized_approach_all_positive_elements(self):
        self.assertEqual(40, find_max_product_optimized_approach([1, 2, 8, 3, 5]))

    def test_optimized_approach_negative_elements(self):
        self.assertEqual(40, find_max_product_optimized_approach([1, 2, -8, -3, -5]))

    def test_optimized_approach_first_element_max(self):
        self.assertEqual(50, find_max_product_optimized_approach([10, 2, 5, 2]))
