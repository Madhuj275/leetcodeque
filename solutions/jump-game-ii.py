# Problem: Jump Game II
# Difficulty: Unknown
# Solution:

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        ending_pos = 0
        curr_pos = 0
        
        for i in range(len(nums) - 1):
            curr_pos = max(curr_pos, i + nums[i])
            if i == ending_pos:
                jumps += 1
                ending_pos = curr_pos
        
        return jumps
        