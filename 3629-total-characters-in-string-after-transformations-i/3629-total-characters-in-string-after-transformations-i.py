from collections import Counter

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        count = Counter(s)
        length = len(s)
        
        for _ in range(t):
            new_count = [0] * 26
            for i in range(25): 
                new_count[i + 1] += count[chr(i + ord('a'))]
            z_count = count['z']
            if z_count > 0:
                new_count[0] += z_count
                new_count[1] += z_count
                length += z_count  
                
            count = {chr(i + ord('a')): new_count[i] % MOD for i in range(26)}
            length = length % MOD
        
        return length
