class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        temp=nums+nums
        res=[-1]*len(temp)
        st=[]
        for i in range(len(temp)):
            while st and temp[st[-1]] < temp[i]:
                res[st.pop()]=temp[i]
            st.append(i)
        return res[0:len(nums)]

        