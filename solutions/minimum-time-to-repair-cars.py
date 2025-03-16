# Problem: Minimum Time to Repair Cars
# Difficulty: Unknown
# Solution:

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        res = -1
        max_rank = max(ranks)
        r = max_rank * cars * cars
        
        while l <= r:
            m = (l + r) // 2
            count = 0
            for rank in ranks:
                count += int(sqrt(m / rank))
            
            if count >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1
                
        return res

        

        