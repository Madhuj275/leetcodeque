# Problem: Largest Number
# Difficulty: Unknown
# Solution:

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        digits = list(map(str, nums))
        digits.sort(reverse=True,key=lambda x: x * 10)
        result = ''.join(map(str, digits))
        return '0' if result[0] == '0' else result
        