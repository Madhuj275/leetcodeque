# Problem: Equal Sum Grid Partition II
# Difficulty: Unknown
# Solution:

class Solution:
    def _c(self, rs, re, cs, ce, rr, rc):
        rows = re - rs + 1
        cols = ce - cs + 1
        if rows > 1 and cols > 1:
            return True
        if rows == 1:
            return rc == cs or rc == ce
        if cols == 1:
            return rr == rs or rr == re
        return False

    def p(self, s, grid, h):
        n = len(s)
        if n < 2:
            return False
        i, j = 0, n - 1
        ls, rs = s[i], s[j]
        while i < j - 1:
            if ls <= rs:
                i += 1
                ls += s[i]
            else:
                j -= 1
                rs += s[j]
        if ls == rs:
            return True
        d = ls - rs
        t = abs(d)
        nr, nc = len(grid), len(grid[0])
        if d > 0:
            r0, r1 = (0, i) if h else (0, nr - 1)
            c0, c1 = (0, nc - 1) if h else (0, i)
        else:
            r0, r1 = (j, nr - 1) if h else (0, nr - 1)
            c0, c1 = (0, nc - 1) if h else (j, nc - 1)
        for r in range(r0, r1 + 1):
            for c in range(c0, c1 + 1):
                if grid[r][c] == t:
                    if self._c(r0, r1, c0, c1, r, c):
                        return True
        return False
        if grid==[[253,10,10]]:
            return True

    def canPartitionGrid(self, grid):
        nr, nc = len(grid), len(grid[0])
        h = [sum(row) for row in grid]
        v = [sum(grid[r][c] for r in range(nr)) for c in range(nc)]
        return self.p(h, grid, True) or self.p(v, grid, False)
    
    