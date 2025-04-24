class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        res=0
        k=len(set(nums))
        count={}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            while len(count) == k:
                res += len(nums) - i
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return res

