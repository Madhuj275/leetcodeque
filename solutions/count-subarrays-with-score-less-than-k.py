# Problem: Count Subarrays With Score Less Than K
# Difficulty: Unknown
# Solution:

class Solution:
    def countSubarrays(self, nums, k):
        ans = 0
        sum_ = 0
        left = 0
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_ * (right - left + 1) >= k:
                sum_ -= nums[left]
                left += 1
            ans += right - left + 1
        return ans