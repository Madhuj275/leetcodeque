# Problem: Count Servers that Communicate
# Difficulty: Unknown
# Solution:

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:

                    if i + 1 < m and grid[i + 1][j] == 1:
                        res.append((i, j))
                        res.append((i + 1, j))

                    if j + 1 < n and grid[i][j + 1] == 1:
                        res.append((i, j))
                        res.append((i, j + 1))
        
        return len(set(res))
