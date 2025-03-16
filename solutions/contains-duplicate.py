# Problem: Contains Duplicate
# Difficulty: Unknown
# Solution:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in nums:
            if nums.count(i)>=2:
                return True
        return False