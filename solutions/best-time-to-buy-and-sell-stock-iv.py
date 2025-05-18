# Problem: Best Time to Buy and Sell Stock IV
# Difficulty: Unknown
# Solution:

class Solution:
    def maxProfit(self, k, prices):
        return self.solve(0, 1, prices, 0, k)

    def solve(self, ind, buy, prices, count, k):
        if ind == len(prices):
            return 0
        if count == k:  
            return 0
        profit = 0
        if buy == 1:  
            op1 = -prices[ind] + self.solve(ind + 1, 0, prices, count, k) 
            op2 = self.solve(ind + 1, 1, prices, count, k)  
            profit = max(op1, op2)
        else:  
            op1 = prices[ind] + self.solve(ind + 1, 1, prices, count + 1, k) 
            op2 = self.solve(ind + 1, 0, prices, count, k)  
            profit = max(op1, op2)

        return profit