class Solution:
    def checkValidString(self, s: str) -> bool:
        st=[]
        pr=[]
        for i in range(len(s)):
            if s[i] =='(':
                pr.append(i)
            elif s[i] =='*':
                st.append(i)
            else:
                if pr:
                    pr.pop()
                elif st:
                    st.pop()
                else:
                    return False
        while pr:
            a=pr.pop()
            if not st:
                return False
            b=st.pop()
            if b < a:
                return False
        
        return True
        
        