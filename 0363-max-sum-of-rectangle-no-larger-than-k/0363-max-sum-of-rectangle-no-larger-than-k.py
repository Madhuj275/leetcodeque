class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        m, n = len(matrix), len(matrix[0])

        max_sum = -float('inf')
        
        for left in range(n):
            
            temp = [0] * m
            
            for right in range(left, n):
                
                for i in range(m):
                    temp[i] += matrix[i][right]
                
                cum_sum = 0
                cum_sum_set = sorted([0])
                
                for t in temp:
                    cum_sum += t
                    it = bisect_left(cum_sum_set, cum_sum - k)
                    if it != len(cum_sum_set):
                        max_sum = max(max_sum, cum_sum - cum_sum_set[it])
                    bisect.insort(cum_sum_set, cum_sum)

        return max_sum