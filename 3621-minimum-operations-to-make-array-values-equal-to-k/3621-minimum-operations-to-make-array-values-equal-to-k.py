class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1 
        
        greater = set()
        for num in nums:
            if num > k:
                greater.add(num)

        return len(greater)