import unittest
from typing import List


def find_max_product_bruteforce_approach(nums: List[int]) -> int:
    max_product = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] > max_product:
                max_product = nums[i] * nums[j]

    return max_product


class TestSolution(unittest.TestCase):
    def test_all_positive_elements(self):
        self.assertEqual(40, find_max_product_bruteforce_approach([1, 2, 8, 3, 5]))

    def test_negative_elements(self):
        self.assertEqual(40, find_max_product_bruteforce_approach([1, 2, -8, -3, -5]))
