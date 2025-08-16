class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        st=[]
        count=0
        for i in s:
            if i=='(':
                st.append(i)
                count+=1
                maxi=max(maxi,count)
            elif st and i==')':
                st.pop()
                count-=1
        return maxi
        