# Problem: Tuple with Same Product
# Difficulty: Unknown
# Solution:

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        seen_products = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product in seen_products:
                    count += seen_products[product]
                seen_products[product] += 1
        
        return count * 8
        