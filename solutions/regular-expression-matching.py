# Problem: Regular Expression Matching
# Difficulty: Unknown
# Solution:

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        slen = len(s)
        plen = len(p)
        
        def backtrack(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == slen and j == plen:
                return True
            
            if j == plen:
                return False
            
            match = i < slen and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < plen and p[j + 1] == '*':
                memo[(i, j)] = backtrack(i, j + 2) or (match and backtrack(i + 1, j))
                return memo[(i, j)]
            else:
                if match:
                    memo[(i, j)] = backtrack(i + 1, j + 1)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = False
                    return False
        
        return backtrack(0, 0)