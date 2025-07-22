class Solution:
    from collections import deque
    
    def orangesRotting(self, grid):
        Minute = 0
        Q = deque()
        FreshCount = 0
        M, N = len(grid), len(grid[0])

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    Q.append((i, j))
                elif grid[i][j] == 1:
                    FreshCount += 1

        while Q and FreshCount > 0:
            NumRotting = len(Q)
            for _ in range(NumRotting):
                i, j = Q.popleft()
                for r, c in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                    if 0 <= r < M and 0 <= c < N and grid[r][c] == 1:
                        grid[r][c] = 2
                        FreshCount -= 1
                        Q.append((r, c))
            Minute += 1  
        
        return Minute if FreshCount == 0 else -1