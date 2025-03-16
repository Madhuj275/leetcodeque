# Problem: Search Insert Position
# Difficulty: Unknown
# Solution:

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range (len(nums)):
            if nums[i]==target:
                return i
            else:
                if(target < nums[i]):
                    return i
        return i+1