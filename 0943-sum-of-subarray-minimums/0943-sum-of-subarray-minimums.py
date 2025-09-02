class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        dp = [0] * n
        stack = []   
        ans = 0

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                ple = stack[-1]
                dp[i] = dp[ple] + arr[i] * (i - ple)
            else:
                dp[i] = arr[i] * (i + 1)

            stack.append(i)
            ans = (ans + dp[i]) % MOD

        return ans