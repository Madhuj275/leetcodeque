# Problem: Array Partition
# Difficulty: Unknown
# Solution:

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        tsum=0
        sorted_nums= sorted(nums, reverse=True)
        for i in range(len(nums)):
            pairs = [(sorted_nums[i], sorted_nums[i + 1]) for i in range(0, len(nums), 2)]
        for j in range(len(pairs)):
            a=min(pairs[j])
            tsum+=a
        return tsum