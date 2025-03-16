# Problem: Is Subsequence
# Difficulty: Unknown
# Solution:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count=0
        for i in s:
            if i in t:
                count+=1
            else:
                return False
        if count==len(s):
            return True
        