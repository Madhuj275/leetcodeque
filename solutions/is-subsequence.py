# Problem: Is Subsequence
# Difficulty: Unknown
# Solution:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1
        return j == len(s)
        