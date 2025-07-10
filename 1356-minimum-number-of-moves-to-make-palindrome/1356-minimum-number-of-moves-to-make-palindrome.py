class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        l, r = 0, len(s)-1
        ans = 0
        while len(s) > 2:
            if s[0] != s[-1]:
                nl, nr = s.find(s[-1]), s.rfind(s[0])
                if nl < len(s) - nr - 1: 
                    ans += nl
                    s = s[:nl] + s[nl+1:-1]
                else:
                    ans += len(s) - nr - 1
                    s = s[1:nr] + s[nr+1:]
            else:
                s = s[1:-1]
        return ans