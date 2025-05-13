# Problem: House Robber IV
# Difficulty: Unknown
# Solution:

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        tsum=0
        min_res=float('inf')
        if k == 1:
            return nums[0]
        for i in range(len(nums)):
            j = i + 2
            while j < len(nums):
                tsum = max(nums[i], nums[j])
                min_res = min(min_res, tsum)
                j += 1

        return min_res




        