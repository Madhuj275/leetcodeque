class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        fruitsCount, minFruits = defaultdict(int), min(min(basket1), min(basket2))
        for fruit in basket1:
            fruitsCount[fruit] += 1
        for fruit in basket2:
            fruitsCount[fruit] -= 1
        toBeExchanged, cost = [], 0
        for fruit in fruitsCount:
            if fruitsCount[fruit] % 2:
                return -1
            for num in range(abs(fruitsCount[fruit]) // 2):
                toBeExchanged.append(fruit)
        toBeExchanged.sort()
        for idx in range(len(toBeExchanged) // 2):
            cost += min(minFruits * 2, toBeExchanged[idx])
        return cost