# Problem: Contains Duplicate III
# Difficulty: Unknown
# Solution:

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        list_nums=[]
        for i,num in enumerate (nums):
            list_nums.append((num,i))
        list_nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(abs(list_nums[i][0] - list_nums[j][0])<=t):
                    if(abs(list_nums[j][1] - list_nums[i][1])<=k):
                        return True
                else:
                    break
        return False