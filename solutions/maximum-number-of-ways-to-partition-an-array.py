# Problem: Maximum Number of Ways to Partition an Array
# Difficulty: Unknown
# Solution:

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        prfx_sum = [0] * (n + 1)
        for i in range(n):
            prfx_sum[i + 1] = prfx_sum[i] + nums[i]
            
        left_prfx_count = Counter()
        right_prfx_count = Counter(prfx_sum[1:-1])
        total_sum = prfx_sum[-1]
        ans = right_prfx_count[total_sum // 2] if total_sum % 2 == 0 else 0
    
        for i in range(n):
            if (total_sum + (k - nums[i])) % 2 == 0:
                target = (total_sum + (k - nums[i])) // 2
                left = left_prfx_count[target]
                right = right_prfx_count[target - k + nums[i]]
                ans = max(ans, left + right)
            left_prfx_count[prfx_sum[i + 1]] += 1
            right_prfx_count[prfx_sum[i + 1]] -= 1
        
        return ans