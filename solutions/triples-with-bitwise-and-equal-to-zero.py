# Problem: Triples with Bitwise AND Equal To Zero
# Difficulty: Unknown
# Solution:

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for x in nums: 
            for y in nums: 
                freq[x&y] += 1
        
        ans = 0
        for x in nums: 
            mask = x = x ^ 0xffff
            while x: 
                ans += freq[x]
                x = mask & (x-1)
            ans += freq[0]
        return ans 