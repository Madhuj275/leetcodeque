# Problem: Sort Colors
# Difficulty: Unknown
# Solution:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        while left < right:
            if nums[left] <= nums[right]:
                left+=1
            else:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                right-=1
        
        return nums



        