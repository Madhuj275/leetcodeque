# Problem: Length of Last Word
# Difficulty: Unknown
# Solution:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ll = [list(word) for word in s.split()]
        length =len(ll[-1])
        return length
        