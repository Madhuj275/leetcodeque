class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # list1=list(s)
        # list2=list(t)
        # if len(list1)!=len(list2):
        #     return False
        # a=list(set(list1))
        # b=list(set(list2))
        # if len(a)==len(b):
        #     return True
        # else:
        #     return False
        res={}
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = set()
            res[s[i]].add(t[i])
        
        seen = set()
        for j in res.values():
            temp=list(j)
            if len(temp)>1 or temp[0] in seen:
                return False
            seen.add(temp[0])
        return True

        