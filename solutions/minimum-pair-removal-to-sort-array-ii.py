# Problem: Minimum Pair Removal to Sort Array II
# Difficulty: Unknown
# Solution:

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        pq = []
        decrease = 0 
        lo = list(range(n))
        hi = list(range(n))
        for i, (x, y) in enumerate(pairwise(nums)): 
            if x > y: decrease += 1
            heappush(pq, (x+y, i, i+1, x, y))
        ans = 0 
        while decrease: 
            v, i, j, x, y = heappop(pq)
            if x == nums[i] and y == nums[j]: 
                if nums[i] > nums[j]: decrease -= 1
                hi[i] = hi[j]
                lo[hi[j]] = i
                if i: 
                    prv = lo[i-1]
                    if nums[prv] > nums[i] and nums[prv] <= v: decrease -= 1
                    if nums[prv] <= nums[i] and nums[prv] > v: decrease += 1
                    heappush(pq, (nums[prv]+v, prv, i, nums[prv], v))
                if hi[j]+1 < n: 
                    nxt = hi[j]+1
                    if nums[j] <= nums[nxt] and v > nums[nxt]: decrease += 1
                    if nums[j] > nums[nxt] and v <= nums[nxt]: decrease -= 1
                    heappush(pq, (v+nums[nxt], i, nxt, v, nums[nxt]))
                nums[i] = v
                nums[j] = None
                ans += 1
        return ans 