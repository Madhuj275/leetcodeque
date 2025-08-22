class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            # if i >= 0:
            st.append(i)
            while st and len(st) > 1 and st[-1] < 0 and st[-2] > 0 :
                a=st.pop()
                b=st.pop()
                if abs(a) > b:
                    st.append(a)
                elif abs(a) < b:
                    st.append(b)

        return st if st else []

        