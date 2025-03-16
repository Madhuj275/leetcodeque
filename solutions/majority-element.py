# Problem: Majority Element
# Difficulty: Unknown
# Solution:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > (len(nums)/2) :
                return i
        