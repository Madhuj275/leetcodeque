class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        # if len(piles)==h:
        #     return r
        def k_eats(k):
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            
            return hours <=h
            
        while l < r:
            k=(l+r)//2
            if k_eats(k):
                r=k
            else:
                l=k+1
        
        return r

            

        
        
        
        