# Problem: Remove Duplicates from Sorted Array II
# Difficulty: Unknown
# Solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        element_count = {}
        pos = 0

        for element in nums:
            if element not in element_count:
                element_count[element] = 0

            if element_count[element] < 2:
                nums[pos] = element
                pos += 1
                element_count[element] += 1

        return pos
        