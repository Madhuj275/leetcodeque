class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                if s[j] not in count:
                    count[s[j]] = 1
                else:
                    count[s[j]] += 1
                vals = list(count.values())
                ans += max(vals) - min(vals)
        return ans
