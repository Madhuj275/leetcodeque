# Problem: Rotate Image
# Difficulty: Unknown
# Solution:

class Solution:
    def rotate(self, matrix):
        if not matrix or len(matrix) == 0:
            return
        m = len(matrix)
        result = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                result[j][m - 1 - i] = matrix[i][j]
        matrix[:] = result
