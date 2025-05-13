class Solution:
    def maxIncreasingCells(self, mat):
        m, n, dict1 = len(mat), len(mat[0]), defaultdict(list)

        for i in range(m):
            for j in range(n):
                dict1[mat[i][j]].append([i,j])

        row, col = [0]*m, [0]*n 

        dp = [[0]*n for _ in range(m)]

        for key,val in sorted(dict1.items()):
            for (x,y) in val:
                dp[x][y] = 1 + max(row[x],col[y])
            for (x,y) in val:
                row[x] = max(row[x],dp[x][y])
                col[y] = max(col[y],dp[x][y])

        return max(col) 