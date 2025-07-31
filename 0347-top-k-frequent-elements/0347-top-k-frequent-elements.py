class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        counter=Counter(nums)
        for key,val in counter.items():
            if len(res) < k:    
                heapq.heappush(res,(val,key))
            else:
                heapq.heappushpop(res,(val,key))
        
        return [r[1] for r in res]
        