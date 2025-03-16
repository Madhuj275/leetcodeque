# Problem: Special Array I
# Difficulty: Unknown
# Solution:

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        res=[False]*(len(nums)-1)
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i]%2==0 and nums[i+1] %2 !=0:
                res[i]=True
            elif nums[i]%2!=0 and nums[i+1] %2 ==0:
                res[i]=True
            else:
                return False
        
        for val in nums:
            if not val:
                return False
        return True



        