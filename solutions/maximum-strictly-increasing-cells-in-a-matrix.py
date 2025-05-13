# Problem: Maximum Strictly Increasing Cells in a Matrix
# Difficulty: Unknown
# Solution:

from typing import List
from functools import cache
from math import inf

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        sorted_rows = []
        for i in range(m):
            row = [(mat[i][j], j) for j in range(n)]
            sorted_rows.append(list(sorted(row)))
        sorted_cols = []
        for j in range(n):
            col = [(mat[i][j], i) for i in range(m)]
            sorted_cols.append(list(sorted(col)))
        
        def upper_bound(arr, x):
            l = -1
            r = len(arr)
            while r - l > 1:
                mid = l + (r - l) // 2
                if arr[mid][0] > x:
                    r = mid
                else:
                    l = mid
            return r
        
        @cache
        def go(i, j):
            res = 1
            row = sorted_rows[i]
            rowub = upper_bound(row, mat[i][j])
            val = mat[i][j]
            for ind in range(rowub, len(row)):
                if row[ind][0] != val:
                    res = max(res, 1 + go(i, row[ind][1]))
                    break
            col = sorted_cols[j]
            colub = upper_bound(col, mat[i][j])
            for ind in range(colub, len(col)):
                if col[ind][0] != val:
                    res = max(res, 1 + go(col[ind][1], j))
                    break
            return res

        ans = -inf
        for i in range(m):
            for j in range(n):
                ans = max(ans, go(i, j))
        return ans



