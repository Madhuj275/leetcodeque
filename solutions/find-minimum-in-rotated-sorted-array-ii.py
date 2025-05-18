# Problem: Find Minimum in Rotated Sorted Array II
# Difficulty: Unknown
# Solution:

class Solution:
    def findMin(self, nums):
        nums.sort()
        return nums[0]