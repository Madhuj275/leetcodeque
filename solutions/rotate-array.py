# Problem: Rotate Array
# Difficulty: Unknown
# Solution:

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res=[]
        n=len(nums)
        k %= n
        for i in range(n-k,n):
            res.append(nums[i])
        for i in range(n-k):
            res.append(nums[i])
        nums[:] = res
        return res
        
        