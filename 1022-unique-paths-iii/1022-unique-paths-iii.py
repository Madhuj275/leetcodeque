class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        start,end = () ,()
        path = 2
        # find start square , end square and squares to walk over
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == 0:
                    path += 1

        visited= set()
        def dfs(start,end,curpath):
            # check if square is visited or obstacle
            if start in visited or grid[start[0]][start[1]] == -1:
                return 0
            # check if destination is reached and all nodes are visited 
            if start == end:
                if curpath == path:
                    return 1
                else:
                    return 0
            
            count = 0
            # add square to visited
            visited.add(start)
            #4-directional walks
            for x,y in [(0,1), (0,-1), (-1,0), (1,0)]:
                if 0<=(x + start[0])<ROW and 0<=(y + start[1])<COL:
                    # increment count
                    count += dfs((x + start[0],y + start[1]), end,curpath+1)  
            # remove square from visited
            visited.remove(start)
            return count
        
        return dfs(start,end,1)