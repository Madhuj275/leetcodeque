class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        res=0
        for i in range(len(operations)):
            if operations[i]=="C":
                st.pop()
            elif operations[i]=="D":
                a=2*st[-1]
                st.append(a)
            elif operations[i]=="+":
                b=st[-1]+st[-2]
                st.append(b)
            else:
                st.append(int(operations[i]))
            
        return sum(st)