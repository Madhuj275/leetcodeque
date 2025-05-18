# Problem: Sort Colors
# Difficulty: Unknown
# Solution:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == 0:
                left += 1
            elif nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                right -= 1

        right = len(nums) - 1
        while left <= right:
            if nums[left] == 1:
                left += 1
            elif nums[right] == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                right -= 1
