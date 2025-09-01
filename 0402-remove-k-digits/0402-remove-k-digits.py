class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        if n == k:
            return "0"
        st=[]
        for i in num:
            while st and k and st[-1]>i:
                st.pop()
                k-=1
            
            st.append(i)

        while st and k>0:
            st.pop()
            k-=1
        
        ans="".join(st).lstrip("0")
        return ans if ans!="" else "0" 

        