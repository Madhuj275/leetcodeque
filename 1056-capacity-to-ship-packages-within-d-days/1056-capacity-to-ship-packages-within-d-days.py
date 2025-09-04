class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def finddays(weights,k):
            days=1
            load=0
            for i in range(len(weights)):
                if load + weights[i] > k:
                    days+=1
                    load=weights[i]
                else:
                    load+=weights[i]
                
            return days
        
        def helper(weights,d):
            l=max(weights)
            r=sum(weights)
            while l<=r:
                mid=(l+r)//2
                ttl=finddays(weights,mid)
                if ttl <=d:
                    r=mid-1
                else:
                    l=mid+1
            
            return l
        
        ans=helper(weights,days)
        return ans


        