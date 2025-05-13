import math

class Solution(object):
    def countSubarrays(self, nums):
        count = 0
        for i in range(len(nums) - 2):
            left = nums[i] + nums[i+2]
            right =(float(nums[i+1]) / 2)  
            if left == right:
                count += 1
        return count
