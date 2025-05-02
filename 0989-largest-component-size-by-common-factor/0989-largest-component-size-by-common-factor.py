class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        par = [i for i in range(mx + 1)]
        nums = set(nums)

        def find(u):
            if par[u] != u:
                par[u] = find(par[u])
            return par[u]
    
        def union(u, v):
            if find(u) == find(v):
                return
            par[find(u)] = find(v)

        for i in range(2, mx + 1):
            for j in range(i, mx + 1, i):
                if j in nums:
                    union(i, j)
        return max(Counter(find(num) for num in nums).values())