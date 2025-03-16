# Problem: Maximum Average Subarray I
# Difficulty: Unknown
# Solution:

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k <= 0 or k > len(nums):
            return []  

        max_elem = max(nums) 
        max_index = nums.index(max_elem)  
        n = len(nums)
        valid_subarrays = []
        tsum=0
        max_sum=0
        for i in range(n - k + 1):  
            if i <= max_index < i + k:  
                valid_subarrays.append(nums[i:i + k])  

        for j in range(len(valid_subarrays)):
            tsum=sum(valid_subarrays[j])
            max_sum=max(max_sum,tsum)
        return (max_sum/k)
        