class Solution:
    def rotate(self, matrix):
        if not matrix or len(matrix) == 0:
            return
        m = len(matrix)
        for i in range(m):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
        for i in range(m):
            matrix[i].reverse()   


                
    
