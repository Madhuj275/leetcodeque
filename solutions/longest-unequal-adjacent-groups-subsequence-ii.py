# Problem: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Unknown
# Solution:

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        
        for i in range(1, len(words)):
            if groups[i] != groups[words.index(res[-1])]:
                count = 0
                for a, b in zip(words[i], res[-1]):
                    if a != b:
                        count += 1
                if count == 1:
                    res.append(words[i])

        return res
