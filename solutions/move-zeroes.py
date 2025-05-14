# Problem: Move Zeroes
# Difficulty: Unknown
# Solution:

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[num]= nums[num],nums[i]
                num+=1
        return nums
        