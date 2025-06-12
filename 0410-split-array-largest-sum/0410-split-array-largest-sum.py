from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(nums, k, maxSum):
            current_sum=0
            subarrays=1
            for i in nums:
                current_sum+=i
                if current_sum>maxSum:
                    subarrays+=1
                    current_sum=i
                    if subarrays>k:
                        return False
            return True
        left,right=max(nums),sum(nums)
        while left<right:
            mid=(left+right)//2
            if canSplit(nums, k, mid):
                right=mid
            else:
                left=mid+1
        return left