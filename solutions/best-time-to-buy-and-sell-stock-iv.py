# Problem: Best Time to Buy and Sell Stock IV
# Difficulty: Unknown
# Solution:

class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        dp = [[[-1] * (k + 1) for _ in range(2)] for _ in range(n)]
        return self.solve(0, 1, prices, 0, k, dp)

    def solve(self, ind, buy, prices, count, k, dp):
        if ind == len(prices):
            return 0
        if count == k:
            return 0
        if dp[ind][buy][count] != -1:
            return dp[ind][buy][count]

        profit = 0
        if buy == 1 and count < k:
            op1 = -prices[ind] + self.solve(ind + 1, 0, prices, count, k, dp)
            op2 = self.solve(ind + 1, 1, prices, count, k, dp)
            profit = max(op1, op2)
        else:
            op1 = prices[ind] + self.solve(ind + 1, 1, prices, count + 1, k, dp)
            op2 = self.solve(ind + 1, 0, prices, count, k, dp)
            profit = max(op1, op2)

        dp[ind][buy][count] = profit
        return dp[ind][buy][count]