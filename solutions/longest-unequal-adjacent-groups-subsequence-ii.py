# Problem: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Unknown
# Solution:

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]  
        count=0
        for i in range(1,len(words)):
            if groups[i]!=groups[i-1] :
                res.append(words[i])

        return res


        