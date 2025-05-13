class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        subset=[]
        def back(start):
            if len(subset)==k:
                res.append(subset[:])
            for i in range(start,n+1):
                subset.append(i)
                back(i+1)
                subset.pop()
        back(1)
        return(res)