class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*(n)
        st=[]
        for i,t in enumerate(temperatures):
            while st and st[-1][0] <t:
                st_t,st_i=st.pop()
                ans[st_i]=i-st_i

            st.append((t,i))
        
        return ans
        