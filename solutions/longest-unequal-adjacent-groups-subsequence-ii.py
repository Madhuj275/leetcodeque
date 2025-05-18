# Problem: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Unknown
# Solution:

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        if len(words)==1:
            return words[0]
        for i in range(len(words)):
            if not res:
                for j in range(i):
                    if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                        count = 0
                        for a, b in zip(words[i], words[j]):
                            if a != b:
                                count += 1
                        if count == 1:
                            res.append(words[j])
                            res.append(words[i])
                            break
            else:
                if groups[i] != groups[words.index(res[-1])] and len(words[i]) == len(res[-1]):
                    count = 0
                    for a, b in zip(words[i], res[-1]):
                        if a != b:
                            count += 1
                    if count == 1:
                        res.append(words[i])

        return res
