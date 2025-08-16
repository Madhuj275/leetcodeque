class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        #max_key = max(count, key=count.get)
        heap = [(-co, char) for char, co in count.items()]
        heapq.heapify(heap)
        res=[]
        while heap:
            co, char = heapq.heappop(heap)
            res.extend([char] * (-co))
        
        return ''.join(res)

        