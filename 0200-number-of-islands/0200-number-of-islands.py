from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        if not grid:
            return 0
        di=[(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    q=deque([(i, j)])
                    while q:
                        x, y=q.popleft()
                        if 0<=x < len(grid) and 0<=y<len(grid[0]) and grid[x][y] == '1':
                            grid[x][y]='0'

                            for m,n in di:
                                q.append((x + m, y + n))
            
        return count



        