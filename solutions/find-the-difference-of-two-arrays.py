# Problem: Find the Difference of Two Arrays
# Difficulty: Unknown
# Solution:

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        return [list(set_nums1-set_nums2), list(set_nums2-set_nums1)]
        