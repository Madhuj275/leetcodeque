# Problem: Count Subarrays With Fixed Bounds
# Difficulty: Unknown
# Solution:

class Solution:
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        ans = 0
        mini = maxi = temp = -1
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                temp = i
            if nums[i] == minK:
                mini = i
            if nums[i] == maxK:
                maxi = i
            res = min(maxi, mini) - temp
            ans += max(0, res)
        return ans