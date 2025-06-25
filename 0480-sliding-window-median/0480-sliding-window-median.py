from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) == 0:
            return []
        ar = SortedList(nums[:k])
        is_odd = k % 2 == 0
        medians = [(ar[k//2 - 1] + ar[k//2]) / 2.0 if is_odd else ar[k//2]]
        for i in range(len(nums) - k):
            ar.discard(nums[i])
            ar.add(nums[i + k])
            medians.append((ar[k//2 - 1] + ar[k//2]) / 2.0 if is_odd else ar[k//2])
        return medians