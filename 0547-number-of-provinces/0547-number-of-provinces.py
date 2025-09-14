class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        count=0
        def dfs(c):
            visited.add(c)
            for i,j in enumerate(isConnected[c]):
                if j and i not in visited:
                    dfs(i)
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count+=1

        return count
                

        