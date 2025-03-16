# Problem: Count Prefix and Suffix Pairs I
# Difficulty: Unknown
# Solution:

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):  
                word1, word2 = words[i], words[j]
                if word2.startswith(word1) and word2.endswith(word1):
                    res += 1
        return res