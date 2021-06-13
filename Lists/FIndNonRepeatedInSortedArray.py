"""

Given a Sorted array, such that each number repeats exactly twice except one number, we need to find that number

Example:
Input:{1,1,2,2,3,4,4,5,5}
Output: 3

Expected Time Complexity :O(log(N)) Binary search was applicable

Refer this for solution: https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/

"""


def find_non_repeating_element(input_list):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if low == high:
            return input_list[low]
        else:
            if mid % 2 == 0:
                if input_list[mid] == input_list[mid + 1]:
                    low = mid + 2
                else:
                    high = mid
            else:
                if input_list[mid] == input_list[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
    return None


print(find_non_repeating_element([1, 1, 2, 2, 3, 3, 4, 4, 5]))
print(find_non_repeating_element([1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(find_non_repeating_element([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]))
print(find_non_repeating_element([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]))
#when mid is odd
print(find_non_repeating_element([1, 1, 3, 3, 5, 5, 6, 6, 7, 7, 8]))
print(find_non_repeating_element([1, 1, 3, 5, 5, 6, 6, 7, 7, 8, 8]))

