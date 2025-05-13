# Problem: Set Mismatch
# Difficulty: Unknown
# Solution:

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                res.append(nums[i])
                if nums[i]==i+1:
                    res.append(i+2)
                else:
                    res.append(i+1)
        return res

        