class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        def helper(k):
            ans=0
            for n in nums:
                ans+=math.ceil(n/k)

            return ans <=threshold
        
        while l < r:
            mid=(l+r)//2
            if helper(mid):
                r=mid
            else:
                l=mid+1
        
        return r
        