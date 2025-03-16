# Problem: Maximum Product of Three Numbers
# Difficulty: Unknown
# Solution:

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        product=1
        if not nums:
            return 0
        for i in range(3):
            product*=nums[i]
        return product
        