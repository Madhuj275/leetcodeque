class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count={ord('a'):-1,ord('b'):-1,ord('c'):-1}
        res=0
        r=0
        while r < len(s):
            count[ord(s[r])]=r
            mini=min(count.values())
            res+=mini+1
            r+=1
        return res

        