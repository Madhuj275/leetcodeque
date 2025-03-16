# Problem: Minimum Size Subarray Sum
# Difficulty: Unknown
# Solution:

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        tsum = 0
        min_count = float('inf')

        for i in range(len(nums)):
            tsum += nums[i]

            while tsum >= target:
                min_count = min(min_count, i - left + 1)
                tsum -= nums[left]
                left += 1
        
        return min_count if min_count != float('inf') else 0


        