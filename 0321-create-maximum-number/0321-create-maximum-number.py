class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getSubsequence(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while stack and drop and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]
        
        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            best = max(best, merge(getSubsequence(nums1, i), getSubsequence(nums2, k - i)))
        
        return best