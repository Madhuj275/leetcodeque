# Problem: Find the Highest Altitude
# Difficulty: Unknown
# Solution:

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]
        alt=gain[0]
        resi=0
        
        for i in range(1,len(gain)):
            resi=res[i-1] + alt
            alt=gain[i]
            res.append(resi)
        
        maxi=max(res)
        return maxi
        