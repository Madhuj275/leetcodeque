class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            dp=[0]*len(arr)
            dp[0]=arr[0]
            non=0
            adj=0
            for i in range(1,len(arr)):
                adj=arr[i]
                if i > 1:
                    adj+=dp[i-2]
                
                non=dp[i-1]
        
                dp[i]=max(adj,non) 
            return dp[len(arr)-1]

        arr1=[]
        arr2=[]
        maxi=0
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if i!=0:
                arr1.append(nums[i])
            if i !=len(nums)-1:
                arr2.append(nums[i])
        
        max1=helper(arr1)
        max2=helper(arr2)
        maxi=max(max1,max2)
        return maxi
        
        