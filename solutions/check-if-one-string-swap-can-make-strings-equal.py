# Problem: Check if One String Swap Can Make Strings Equal
# Difficulty: Unknown
# Solution:

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True     
        count=0
        if set(s1) != set(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count+=1
        
        total=count//2
        
        if total > 1:
            return False
        else:
            return True

        