# Problem: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Unknown
# Solution:

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if len(words) == 1:
            return [words[0]]

        if all(g == groups[0] for g in groups):
            return [max(words, key=len)]

        max_chain = []

        for i in range(len(words)):
            temp = [words[i]]
            last_group = groups[i]

            for j in range(i+1, len(words)):
                if groups[j] != last_group and len(words[j]) == len(temp[-1]):
                    count = 0
                    for a, b in zip(words[j], temp[-1]):
                        if a != b:
                            count += 1
                    if count == 1:
                        temp.append(words[j])
                        last_group = groups[j]

            if len(temp) > len(max_chain):
                max_chain = temp

        if max_chain:
            return max_chain


        max_group = max(groups)
        for i in range(len(words)):
            if groups[i] == max_group:
                return [words[i]]
