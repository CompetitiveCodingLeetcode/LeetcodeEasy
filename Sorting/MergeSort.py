"""
code for merge sort in recursive way
"""
from typing import List


class Solution():
    def merge(self,nums: List[int], left:List[int], right:List[int]):

        idx1=idx2=0
        main_array_idx = 0

        while idx1<len(left) and idx2<len(right):
            if left[idx1] <= right[idx2]:
                nums[main_array_idx] = left[idx1]
                idx1 += 1
                main_array_idx += 1
            else:
                nums[main_array_idx] = right[idx2]
                idx2 += 1
                main_array_idx += 1

        while idx1<len(left):
            nums[main_array_idx] = left[idx1]
            idx1+=1
            main_array_idx += 1

        while idx2<len(right):
            nums[main_array_idx] = right[idx2]
            idx2 += 1
            main_array_idx += 1

    def merge_sort(self, nums:List[int]):
        if len(nums) == 1:
            return
        else:
            mid  = len(nums)//2
            left_nums = nums[0:mid]
            right_nums = nums[mid:]

            self.merge_sort(left_nums)
            self.merge_sort(right_nums)

            self.merge(nums,left_nums,right_nums)


solution = Solution()
nums = [9,9,3,4,1,4,23,90,45,67]
solution.merge_sort(nums)
print(nums)

