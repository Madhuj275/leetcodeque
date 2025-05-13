# Problem: Arithmetic Slices
# Difficulty: Unknown
# Solution:

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        if len(nums)==3:
            return 1
        prev=nums[1] - nums[0] 
        count=0
        res=0
        for i in range(1,len(nums)):
            curr=nums[i]-nums[i-1]
            if curr == prev:
                res+=count
                count+=1
            else:
                prev=curr
                count =1
            
        return res
        