class Solution:
    def findMin(self, nums):
        N=len(nums)
        start=0
        end=N-1
        while start<end:
            mid=(start+end)//2
            while nums[mid]==nums[end] and mid<end:
                end-=1
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        return nums[start]