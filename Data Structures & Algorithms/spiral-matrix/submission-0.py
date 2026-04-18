class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        top = 0 
        bottom = len(matrix)      
        left = 0 
        right = len(matrix[0])
        
        

        total_nums = len(matrix) * len(matrix[0])
        out = []
        counter = 0
        while top < bottom and left < right:


            # left to right 
            for i in range(left, right):
                out.append(matrix[top][i])
                counter += 1

            top += 1 

            # top to bottom 
            for i in range(top, bottom):
                out.append(matrix[i][right-1])
                counter += 1

            right -= 1 

            if not (left < right and top < bottom):
                break

            # right to left
            for i in range(right - 1, left-1, -1):
                out.append(matrix[bottom-1][i])
                counter += 1
            bottom -= 1 
  
            # # bottom to top 
            for i in range(bottom-1, top-1, -1):
                out.append(matrix[i][left])
                counter += 1
            left += 1 

            print(out)
            print(counter)

        return out