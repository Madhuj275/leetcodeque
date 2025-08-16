class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s=list(s)
        list_t=list(t)
        s1=Counter(list_s)
        s2=Counter(list_t)
        if s1==s2 and len(s)==len(t):
            return True
        else:
            return False
        