class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi=1
        c=1
        nums=list(set(nums))
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] ==nums[i-1] +1:
                c+=1
                maxi=max(maxi,c)
            else:
                c=1
        return maxi
