class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        op=0
        for i in range(0,len(nums),3):
            s=set(nums[i:])
            if len(s)==n-i:
                break
            else:
                op+=1
        return op


        