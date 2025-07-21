class Solution:
    def makeFancyString(self, s: str) -> str:
        st=list(s)
        count=1
        res=[]
        res.append(st[0])
        for i in range(1,len(st)):
            if st[i]==st[i-1]:
                count+=1
            else:
                count=1
            if count < 3:
                res.append(st[i])
        return ''.join(res)


        
        