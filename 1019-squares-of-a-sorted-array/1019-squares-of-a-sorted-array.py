class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            a=nums[i]**2
            res.append(a)
        
        res.sort()
        return res


        