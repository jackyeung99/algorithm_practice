class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        
        # flip matrix
        for row in range(len(matrix)//2):

            first_row = matrix[row]
            last_row = matrix[len(matrix) - row - 1]

            matrix[row] = last_row 
            matrix[len(matrix) - row - 1] = first_row

        # transpose 
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                val = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = val
