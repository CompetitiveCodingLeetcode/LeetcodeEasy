"""

"""
from typing import List
class Solution():
    def find_subsets(self,nums:List[int],output:List[int],index:int,ans:List[List[int]]):
        if index>=len(nums):
            #TODO: need to check why output.copy() is used
            if len(output) > 1:
                ans.append(output.copy())
            return

        else:

            #include call
            element = nums[index]
            output.append(element)
            self.find_subsets(nums,output,index+1,ans)
            output.pop()
            # exclude call
            self.find_subsets(nums, output, index + 1, ans)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        index=0
        output=[]
        ans=[]
        self.find_subsets(nums,output,index,ans)
        return ans

obj = Solution()
print(obj.subsets([5,1,4,3,2,1]))