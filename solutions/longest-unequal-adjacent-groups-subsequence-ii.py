# Problem: Longest Unequal Adjacent Groups Subsequence II
# Difficulty: Unknown
# Solution:

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if len(words) == 1:
            return [words[0]]

        if all(g == groups[0] for g in groups):
            longest = max(words, key=len)
            return [longest]

        max_res = []

        for start in range(len(words)):
            temp = [words[start]]
            for i in range(start + 1, len(words)):
                last_word = temp[-1]
                last_group = groups[words.index(last_word)]

                if groups[i] != last_group and len(words[i]) == len(last_word):
                    count = 0
                    for a, b in zip(words[i], last_word):
                        if a != b:
                            count += 1
                    if count == 1:
                        temp.append(words[i])

            if len(temp) > len(max_res):
                max_res = temp

        if max_res:
            return max_res

        max_group = max(groups)
        for i in range(len(words)):
            if groups[i] == max_group:
                return [words[i]]
