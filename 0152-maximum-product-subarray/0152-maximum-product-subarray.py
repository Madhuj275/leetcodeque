class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        mini=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            temp=maxi
            maxi=max(nums[i],max(maxi*nums[i],mini*nums[i]))
            mini=min(nums[i],min(temp*nums[i],mini*nums[i]))
            ans=max(ans,maxi)
        
        return ans


            



        