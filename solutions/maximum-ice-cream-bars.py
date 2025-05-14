# Problem: Maximum Ice Cream Bars
# Difficulty: Unknown
# Solution:

class Solution:
    def maxIceCream(self, costs, coins):
        heapify(costs)
        n_bar = 0
        while costs:
            coins -= heappop(costs)
            if coins<0: return n_bar
            n_bar += 1
        return n_bar