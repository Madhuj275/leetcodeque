class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        for i in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,i)
            else:
                heapq.heappushpop(min_heap,i)
        return min_heap[0]
        