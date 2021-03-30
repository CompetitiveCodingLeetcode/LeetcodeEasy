"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?



Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1



Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.


"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element_count_dict = {}
        for num in range(0, len(nums)):
            if nums[num] in element_count_dict:
                element_count_dict[nums[num]] += 1
            else:
                element_count_dict[nums[num]] = 1

        for key, value in element_count_dict.items():
            if value == 1:
                return key


    def mathematical_approach(self,nums: List[int]) -> int:

        """

        :param nums:
        :return:

        2∗(a+b+c)−(a+a+b+b+c)=c2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c


        does not work for the case where the occurrence for the numbers is more thsn 2
        """
        return 2*sum(set(nums)) - sum(nums)


    """
    
    If we take XOR of zero and some bit, it will return that bit
        a⊕0=a
    If we take XOR of two same bits, it will return 0
        a⊕a=0
    a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

    """
    def bit_manipulation_approach(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


obj=Solution()
print(obj.singleNumber([2,2,1]))



print(obj.mathematical_approach([2,2,1]))

print(obj.bit_manipulation_approach([4,1,2,1,2]))