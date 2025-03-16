# Problem: Maximum Gap
# Difficulty: Unknown
# Solution:

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        maxi=0
        res=0
        for i in range(len(nums)-1):
            res=nums[i+1] - nums[i]
            maxi = max(maxi,res)
        return maxi
        