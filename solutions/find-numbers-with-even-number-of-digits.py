# Problem: Find Numbers with Even Number of Digits
# Difficulty: Unknown
# Solution:

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            digits = 0
            while x > 0:
                digits += 1
                x //= 10
            if (digits%2) == 0:
                count += 1
        return count