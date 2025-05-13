DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        to_check = list(sorted(set(queries), reverse=True))
        m, n = len(grid), len(grid[0])
        
        result = {}
        q = [(grid[0][0], 0, 0)]
        grid[0][0] = -1
        k = 0
        
        for c in to_check[::-1]:
            while q and q[0][0] < c:
                y, i, j = heapq.heappop(q)
                k += 1
                for di, dj in DIRECTIONS:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] > -1 and grid[ii][jj] < to_check[0]:
                        heapq.heappush(q, (grid[ii][jj], ii, jj))
                        grid[ii][jj] = -1
            result[c] = k
        
        return [result[x] for x in queries]
       