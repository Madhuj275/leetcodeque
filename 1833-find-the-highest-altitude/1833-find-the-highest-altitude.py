class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] 
        alt = 0 
        for i in range(len(gain)):
            alt += gain[i] 
            res.append(alt) 
        
        maxi = max(res)  
        return maxi