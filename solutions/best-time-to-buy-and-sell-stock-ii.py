# Problem: Best Time to Buy and Sell Stock II
# Difficulty: Unknown
# Solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        start = prices[0]
        n = len(prices)
        for i in range(n):
            if start < prices[i]: 
                maxi += prices[i] - start
            start = prices[i]
        return maxi
        