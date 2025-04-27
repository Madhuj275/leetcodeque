# Problem: Count Subarrays of Length Three With a Condition
# Difficulty: Unknown
# Solution:

import math
class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 2):  
            if nums[i] + nums[i+2] == math.floor(nums[i+1] / 2):
                count += 1

        return count
