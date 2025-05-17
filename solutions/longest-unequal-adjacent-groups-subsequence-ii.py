# Problem: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Unknown
# Solution:

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if n == 1:
            return [words[0]]
        if all(g == groups[0] for g in groups):
            return [max(words, key=len)]
        
        memo = [[words[i]] for i in range(n)]
        
        for i in range(n):
            for j in range(i):

                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    count = 0
                    for a, b in zip(words[i], words[j]):
                        if a != b:
                            count += 1
                            if count > 1:
                                break
                    if count == 1 and len(memo[j]) + 1 > len(memo[i]):
                        memo[i] = memo[j] + [words[i]]
        
        best = max(memo, key=len)
        if len(best) > 1:
            return best
 
        max_group = max(groups)
        for i in range(n):
            if groups[i] == max_group:
                return [words[i]]
