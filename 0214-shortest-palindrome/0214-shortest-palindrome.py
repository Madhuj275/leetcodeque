class Solution:
    def shortestPalindrome(self, s):
        r = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i] + s