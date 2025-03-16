# Problem: Longest Strictly Increasing or Strictly Decreasing Subarray
# Difficulty: Unknown
# Solution:

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0   
        max_length = 1
        inc_length = 1
        dec_length = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:  
                inc_length += 1
                dec_length = 1  
            elif nums[i] < nums[i - 1]:  
                dec_length += 1
                inc_length = 1  
            else:
                inc_length = 1
                dec_length = 1  

            max_length = max(max_length, inc_length, dec_length)

        return max_length



            

        