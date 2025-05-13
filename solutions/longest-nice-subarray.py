# Problem: Longest Nice Subarray
# Difficulty: Unknown
# Solution:

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        current = 0
        left = 0
        for right in range(len(nums)):
            while current & nums[right]:
                current ^= nums[left]   
                left += 1
            
            current |= nums[right]  
            res = max(res, right - left + 1)

        return res
