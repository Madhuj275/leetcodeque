# Problem: House Robber IV
# Difficulty: Unknown
# Solution:

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tsum=0
        min_res=float('inf')
        if k == 1:
            return nums[0]
        
        for i in range(n - 1): 
            j = i + 2
            while j < n:
                min_res = min(min_res, max(nums[i], nums[j]))
                j+=1

        return min_res




        