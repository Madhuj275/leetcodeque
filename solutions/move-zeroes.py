# Problem: Move Zeroes
# Difficulty: Unknown
# Solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp = []
        for i in nums[:]:
            if i == 0:
                temp.append(i)
                nums.remove(i)
        nums = nums.extend(temp)
        

        
        
                
        