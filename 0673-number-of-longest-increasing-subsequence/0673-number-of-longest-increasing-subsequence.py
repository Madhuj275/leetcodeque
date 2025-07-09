class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        res=[1]*len(nums)
        counts=[1]*len(nums)
        ans=0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if res[j]+1> res[i]:
                        res[i]=res[j]+1
                        counts[i]=counts[j]
                    elif res[j]+1==res[i]:
                        counts[i]+=counts[j]

        maxi=max(res)
        for i in range(len(res)):
            if res[i]==maxi:
                ans+=counts[i]

        return ans    