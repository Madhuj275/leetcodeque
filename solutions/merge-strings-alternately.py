# Problem: Merge Strings Alternately
# Difficulty: Unknown
# Solution:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        l_word1=list(word1)
        l_word2=list(word2)
        a=len(l_word1)
        b=len(l_word2)
        if len(l_word1) > len(l_word2):
            for i in range(len(l_word2)):
                res.append(l_word1[i])
                res.append(l_word2[i])
                # l_word1.remove(l_word1[i])
            res+=l_word1[b:a]
        elif len(l_word1) < len(l_word2):
            for i in range(len(l_word1)):
                res.append(l_word1[i])
                res.append(l_word2[i])
                # l_word2.remove(l_word2[i])
            res+=l_word2[a:b]
        else:
            for i in range(len(l_word1)):
                res.append(l_word1[i])
                res.append(l_word2[i])
        result = ''.join(res)
        return result

        