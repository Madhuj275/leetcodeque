# Problem: Find the Difference of Two Arrays
# Difficulty: Unknown
# Solution:

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        unique_list1 = list(set([num for num in nums1 if  num not in count2]))
        unique_list2 = list(set([num for num in nums2 if  num not in count1]))
        return[unique_list1,unique_list2]
        