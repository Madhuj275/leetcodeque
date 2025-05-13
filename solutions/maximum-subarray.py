# Problem: Maximum Subarray
# Difficulty: Unknown
# Solution:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        ts=0
        for i in range(len(nums)):
            ts+=nums[i]
            if ts > maxi:
                maxi=ts
            elif ts < 0:
                ts=0
        return maxi