import math
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mat = [num for row in grid for num in row]
        mat.sort()
        a = mat[len(mat) // 2]
        count = 0
        for i in mat:
            if abs(i - a) % x != 0:
                return -1
            count += abs(i - a) // x
        return count




        