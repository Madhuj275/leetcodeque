# Problem: Palindrome Number
# Difficulty: Unknown
# Solution:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        while (temp>0):
            reverse = reverse * 10 + temp % 10
            temp//=10
        return  reverse == x