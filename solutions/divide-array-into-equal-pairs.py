# Problem: Divide Array Into Equal Pairs
# Difficulty: Unknown
# Solution:

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0  
            count[n] += 1  
        
        res = True
        for value in count.values():  
            if value % 2 != 0:
                res = False
                break
        
        return res
        

        