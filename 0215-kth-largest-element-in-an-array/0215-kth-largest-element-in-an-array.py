class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):
        #     nums[i]=-nums[i]
        n=len(nums)
        heapq.heapify(nums)
        
        for i in range(n-k-1,-1,-1):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
        