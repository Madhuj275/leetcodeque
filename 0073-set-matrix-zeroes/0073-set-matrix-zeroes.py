class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_i=set()
        zero_j=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zero_i.add(i)
                    zero_j.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_i or j in zero_j:
                    matrix[i][j]=0
        
        return matrix
