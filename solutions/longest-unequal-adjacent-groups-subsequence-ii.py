# Problem: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Unknown
# Solution:

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        for i in range(len(words)):
            if not res:
                res.append(words[i])
            else:
                if groups[i] != groups[words.index(res[-1])]:
                    if len(words[i]) == len(res[-1]):
                        count = 0
                        for a, b in zip(words[i], res[-1]):
                            if a != b:
                                count += 1
                        if count == 1:
                            res.append(words[i])

        return res
