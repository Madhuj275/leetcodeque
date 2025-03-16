# Problem: Next Greater Element I
# Difficulty: Unknown
# Solution:

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num in nums2:
                j = nums2.index(num) + 1
                if j < len(nums2) and nums2[j] > num:
                    res.append(nums2[j])
                else:
                    res.append(-1)
        return res