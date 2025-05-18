# Problem: Total Characters in String After Transformations I
# Difficulty: Unknown
# Solution:

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
            new_count[0] += z_count  
            new_count[1] += z_count  
            new_count = [x % MOD for x in new_count]
            count = {chr(i + ord('a')): new_count[i] for i in range(26)}
            length = sum(new_count) 

        return length
