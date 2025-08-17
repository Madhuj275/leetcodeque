class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        dp=[0]*len(nums)
        dp[0]=nums[0]
        non=0
        adj=0
        for i in range(1,len(nums)):
            adj=nums[i]
            if i > 1:
                adj+=dp[i-2]
            
            non=dp[i-1]
     
            dp[i]=max(adj,non) 
        return dp[len(nums)-1]
        

        