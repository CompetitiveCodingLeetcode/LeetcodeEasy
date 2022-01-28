import unittest
from typing import List


def swap(i: int, j: int, nums: List[int]):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


# Two-pointer approach (Single traversal approach) complexity O(n)
def sort0s1s(nums: List[int]) -> List[int]:
    i = 0
    j = len(nums) - 1

    while i < j:
        while nums[i] == 0:
            i += 1
        while nums[j] == 1:
            j -= 1
        swap(i, j, nums)
        i += 1
        j -= 1

    return nums


class TestSolution(unittest.TestCase):

    def test_sort0s1s_case1(self):
        self.assertListEqual(sort0s1s([1, 0, 0, 1]), [0, 0, 1, 1])

    def test_sort0s1s_case2(self):
        self.assertListEqual(sort0s1s([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_sort0s1s_case3(self):
        self.assertListEqual(sort0s1s([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_sort0s1s_case4(self):
        self.assertListEqual(sort0s1s([1]), [1])

    def test_sort0s1s_case5(self):
        self.assertListEqual(sort0s1s([0]), [0])

    def test_sort0s1s_case6(self):
        self.assertListEqual(sort0s1s([0, 1, 1, 1, 1, 1, 0, 0]), [0, 0, 0, 1, 1, 1, 1, 1])

    def test_sort0s1s_large_input(self):
        self.assertListEqual(sort0s1s(
            [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
             1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
             0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1,
             1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0,
             1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0,
             1, 0, 1, 0, 0, 1]),
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1])
