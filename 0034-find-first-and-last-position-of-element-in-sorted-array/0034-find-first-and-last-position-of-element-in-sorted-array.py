class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    right = mid - 1
            return ans
        
        def findRight():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    left = mid + 1
            return ans
        
        left = findLeft()
        right = findRight()
        return [left, right] if left != -1 else [-1, -1]
