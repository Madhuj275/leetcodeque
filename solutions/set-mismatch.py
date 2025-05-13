# Problem: Set Mismatch
# Difficulty: Unknown
# Solution:

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                res.append(nums[i])
                res.append (i+1)
        return res

        