# Problem: Minimum Operations to Make a Uni-Value Grid
# Difficulty: Unknown
# Solution:

import math
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mat=[num for row in grid for num in row]
        mat.sort()
        count=0
        a=math.ceil(mat[-1]/2)
        for i in mat:
            diff = abs(i - a)
            if diff % x != 0:
                return -1
            count += diff // x
        return count




        