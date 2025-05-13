# Problem: Arithmetic Slices
# Difficulty: Unknown
# Solution:

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        prev=0
        count=0
        res=[]
        for i in range(1,len(nums)):
            curr=abs(nums[i]-nums[i-1])
            if curr == prev:
                res.append(nums[i-1])
                count+=1
            else:
                prev=curr
                count+=1
            
        return len(res) + 1
        