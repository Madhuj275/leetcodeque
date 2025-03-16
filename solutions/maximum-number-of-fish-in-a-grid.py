# Problem: Maximum Number of Fish in a Grid
# Difficulty: Unknown
# Solution:

from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        max_fish = 0

        def bfs(x, y):
            queue = deque([(x, y)])
            total_fish = 0

            while queue:
                cx, cy = queue.popleft()
                total_fish += grid[cx][cy]
                grid[cx][cy] = 0 

                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 0:
                        queue.append((nx, ny))

            return total_fish

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:  
                    max_fish = max(max_fish, bfs(i, j))

        return max_fish