class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        maxi=0
        if not grid:
            return 0
        di=[(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count=0
                    q=deque([(i, j)])
                    while q:
                        x, y=q.popleft()
                        if 0<=x < len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                            grid[x][y]=0
                            count+=1
                            for m,n in di:
                                q.append((x + m, y + n))
                    maxi=max(maxi,count)
        return maxi
        