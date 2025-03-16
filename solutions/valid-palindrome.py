# Problem: Valid Palindrome
# Difficulty: Unknown
# Solution:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=[char.lower() for char in s if char.isalpha()]
        if len(chars)==0:
            return True
        n=len(chars)
        i=0
        j=n-1
        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1
            
        return True
        


        