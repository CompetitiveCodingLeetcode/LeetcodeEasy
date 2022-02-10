"""

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]



Constraints:

    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6


"""
from typing import List
import time

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_val= 0
        sum_list=[]
        start = time.time()
        for num in nums:
            sum_val+=num
            sum_list.append(sum_val)
        end = time.time()
        print("time taken=",end-start)#3.814697265625e-06
        return sum_list

    def approach2(self,nums: List[int]) -> List[int]:
        start = time.time()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        end = time.time()
        print("time taken=",end-start)#8.58306884765625e-06
        return nums

obj=Solution()
print(obj.runningSum([3,9,1,2]))
print(obj.approach2([3,9,1,2]))
