# Problem: Check if Array Is Sorted and Rotated
# Difficulty: Unknown
# Solution:

class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt=0
        for i in range(len(nums)):
            if(nums[(i-1) % len(nums)] > nums[i]):
                cnt+=1
        if cnt > 1:
            return False
        else:
            return True
        