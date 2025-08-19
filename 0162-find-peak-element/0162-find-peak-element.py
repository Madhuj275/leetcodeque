class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a=max(nums)
        return nums.index(a)
        