# Problem: Maximum Ascending Subarray Sum
# Difficulty: Unknown
# Solution:

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum=0
        tsum=nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] >= nums[i] :
                tsum+=nums[i+1]
                maxsum=max(maxsum,tsum)
            else:
                tsum=nums[i+1]
        return maxsum


        