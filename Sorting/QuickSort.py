from typing import List


class Solution():
    def swap(self,nums:List[int],i:int,j:int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def partition(self,nums:List[int],start:int,end:int)->int:
        pivot = nums[start]
        count = 0

        #find correct pos
        for i in range(start+1,end+1):
            if nums[i] <= pivot:
                count += 1

        pivot_idx = start+count
        # swap to put the pivot element to correct position
        self.swap(nums,start,pivot_idx)

        i=start
        j=end

        while(i<pivot_idx and j>pivot_idx):
            while(nums[i]<pivot):
                i+=1
            while(nums[j]>pivot):
                j-=1

            if i<pivot_idx and j>pivot_idx:
                self.swap(nums,i,j)
                i+=1
                j-=1
        return pivot_idx



    def quick_sort(self, nums: List[int],start: int, end:int):
        if start>=end:
            return

        p = self.partition(nums,start,end)
        self.quick_sort(nums,start,p-1)
        self.quick_sort(nums,p+1,end)

solution=Solution()
nums=[2,5,1,43,45,23,0,7,65,78,4,3,3,3]
nums1=[1,1,1,1,0]
solution.quick_sort(nums,0,13)
solution.quick_sort(nums1,0,4)
print(nums)
print(nums1)