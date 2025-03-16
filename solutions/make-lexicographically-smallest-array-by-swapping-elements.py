# Problem: Make Lexicographically Smallest Array by Swapping Elements
# Difficulty: Unknown
# Solution:

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        for i in range(len(nums)-1):
            j=i+1
            if abs(nums[i]-nums[j]) <= limit:
                nums[i], nums[j] = nums[j], nums[i]
        return nums

