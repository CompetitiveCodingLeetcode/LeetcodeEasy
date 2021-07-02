from typing import List


class Solution:
    def calculate(self, nums, k, max_len, s, nums_len):
        if nums[s:] == []:
            print("max_len=",max_len)
            return max_len
        else:
            i = 0
            temp = k
            ans = []
            temp_nums = nums[s:]
            print("nums=", temp_nums)
            while i != len(temp_nums):
                if temp == 0 and temp_nums[i] == 0:
                    break
                else:
                    print("*=", temp_nums[i])
                    if temp_nums[i] == 1:
                        ans.append(temp_nums[i])
                    elif temp_nums[i] == 0:
                        temp = temp - 1
                        ans.append(1)
                i += 1
            print("###########################")
            max_len = max(max_len, len(ans))
            print("max=",max_len)
            s = s + 1
            print("s=",s)
            self.calculate(nums, k, max_len, s, nums_len)

    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        max_len = self.calculate(nums, k, max_len, 0, len(nums))
        # print(max_len)


obj = Solution()
obj.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)
obj.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)