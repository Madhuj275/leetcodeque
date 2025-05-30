# Problem: Trapping Rain Water
# Difficulty: Unknown
# Solution:

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left, right = 0, n - 1  
        max_left, max_right = 0, 0  
        trapped = 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    trapped += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    trapped += max_right - height[right]
                right -= 1
        
        return trapped

        