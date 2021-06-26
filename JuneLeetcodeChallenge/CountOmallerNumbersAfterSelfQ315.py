"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:

Input: nums = [-1]
Output: [0]

Example 3:

Input: nums = [-1,-1]
Output: [0,0]



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

For better approach:
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/408322/Python-Different-Concise-Solutions

"""
# Approach:
# iterate each element
# 5,2,6,1
# i = 0 to len
# 5
# count = 0
# i+1 - end of list --- if i != len-1


from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count_list = []
        for i in range(0,len(nums)):
            count = 0
            if i == len(nums) - 1:
                count_list.append(count)
            else:
                for j in range(i+1,len(nums)):
                    if nums[j] < nums[i]:
                        count +=1
                count_list.append(count)
        return count_list

obj = Solution()
print(obj.countSmaller([5,2,6,1]))
print(obj.countSmaller([-1]))
print(obj.countSmaller([-1,-1]))

