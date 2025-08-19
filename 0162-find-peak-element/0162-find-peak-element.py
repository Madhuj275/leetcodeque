class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        left=1
        right=n-2
        while left <=right:
            mid =left+(right-left)//2
            if nums[mid]> nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid]< nums[mid-1]:
                right=mid-1
            elif nums[mid]<nums[mid+1]:
                left=mid+1
        


        