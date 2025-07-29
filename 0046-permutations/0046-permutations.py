class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        temp=[]
        def backtrack():
            if len(temp)==n:
                res.append(temp[:])
                return
            
            for i in nums:
                if i not in temp:
                    temp.append(i)
                    backtrack()
                    temp.pop()

        backtrack()  
        return res

        