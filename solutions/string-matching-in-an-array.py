# Problem: String Matching in an Array
# Difficulty: Unknown
# Solution:

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[(s1) for s1 in words for s2 in words if s1 != s2 and s1 in s2]
        return res