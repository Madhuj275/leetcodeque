from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        count = [0] * (n + 1)  

        for start, end in queries:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1

        for i in range(1, n):
            count[i] += count[i - 1]

        for i in range(n):
            nums[i] -= min(nums[i], count[i])

        return sum(nums) == 0
