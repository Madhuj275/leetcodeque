# Problem: Count Subarrays of Length Three With a Condition
# Difficulty: Unknown
# Solution:

import math

class Solution(object):
    def countSubarrays(self, nums):
        count = 0
        for i in range(len(nums) - 2):
            left = nums[i] + nums[i+2]
            right = math.ceil(float(nums[i+1]) / 2)  
            if left == right:
                count += 1
            if left==0 and right==1:
                count+=1
        return count
