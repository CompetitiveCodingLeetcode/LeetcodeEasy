"""
given an array of integers from 1 to 100.
Find he missing element

Approach:
sum = n(n+1)/2

missing element = sum - total_sum_of_list
"""


def missingElement(nums: list) -> int:
    total_sum = sum(nums)
    n = len(nums) + 1
    actual_sum = (n * (n + 1)) / 2

    return int(actual_sum - total_sum)


print(missingElement([1, 2, 3, 4, 6]))
