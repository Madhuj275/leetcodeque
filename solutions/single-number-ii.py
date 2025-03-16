# Problem: Single Number II
# Difficulty: Unknown
# Solution:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if nums.count(i) ==1:
                return i
        