# Problem: Sorted GCD Pair Queries
# Difficulty: Unknown
# Solution:

class Solution:
    def gcdValues(self, nums, queries):
        mxN = max(nums) + 10
        mob = [0] * mxN
        sve = [0] * mxN
        cnt = [0] * mxN
        mob[1] = 1

        for num in nums:
            cnt[num] += 1

        for i in range(1, mxN):
            sve[i] += cnt[i]
            for j in range(2 * i, mxN, i):
                mob[j] -= mob[i]
                sve[i] += cnt[j]

        def solve(i):
            return sum(mob[j // i]  * sve[j] * (sve[j]-1) // 2 for j in range(i, mxN, i))

        
        ans = [0] * len(queries)
        q = sorted([(queries[i], i) for i in range(len(queries))])

        i, j, cur = 1, 0, solve(1) - 1

        while j < len(q):
            while cur < q[j][0]:
                i += 1
                cur += solve(i)
            ans[q[j][1]] = i
            j += 1

        return ans