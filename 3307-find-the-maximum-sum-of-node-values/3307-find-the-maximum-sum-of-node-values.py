class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res = 0

        count_xor = 0
        for num in nums:
            if num < num ^ k:
                res += num ^ k
                count_xor += 1
            else:
                res += num

        if count_xor % 2 == 1:
            min_xor = res
        
            for num in nums:
                min_xor = min(min_xor, abs(num - (num ^ k)))
            
            res -= min_xor
        
        return res

