class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*10000
        st=[]

        for num in nums2:
            while st and st[-1] < num:
                res[st.pop()]=num
            st.append(num)

        return [res[num] for num in nums1]
