# Problem: Two Sum
# Difficulty: Unknown
# Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)-1):
            if(nums[i]+nums[i+1]==target):
                res.append(i)
                res.append(i+1)
                return res
            
        return [-1,-1]
        