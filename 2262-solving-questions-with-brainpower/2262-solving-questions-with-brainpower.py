class Solution:
    def mostPoints(self, arr: List[List[int]]) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            skip = dp[i + 1] if i + 1 < n else 0
            pick = arr[i][0]
            if i + 1 + arr[i][1] < n:
                pick += dp[i + 1 + arr[i][1]]
            dp[i] = max(skip, pick)

        return dp[0]