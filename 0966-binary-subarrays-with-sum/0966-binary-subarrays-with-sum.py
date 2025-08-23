class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=defaultdict(int)
        res[0]=1
        ans=0
        prefixsum=0
        for i in nums:
            prefixsum+=i
            ans+=res[prefixsum-goal]
            res[prefixsum]+=1
        return ans