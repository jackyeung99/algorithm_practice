class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        visited = [[False] * cols for _ in range(rows)]
        
        def bfs(row, col):

            q = deque([(row, col)]) 

            char = board[row][col]
            while q:
                row, col = q.popleft()


                for dr, dc in directions:
                    
                    new_row = dr + row 
                    new_col = dc + col 

                    if 0 <= new_col < cols and 0 <= new_row < rows and board[new_row][new_col] == char and not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        q.append((new_row, new_col))




        for row in range(rows): 
            # if not visited[row][col]:
            visited[row][0] = True
            visited[row][cols-1] = True
            bfs(row, 0)
            bfs(row, cols-1)

        
        for col in range(1, cols-1): 
            # if not visited[row][col]:
            visited[0][col] = True
            visited[rows-1][col] = True
            bfs(0, col)
            bfs(rows-1, col)
        
        for x in visited:
            print(x)

        for x in board:
            print(x)

        for row in range(rows):
            for col in range(cols):

                if not visited[row][col] and board[row][col] == 'O':
                    board[row][col] = 'X'   


        # ['X', 'O', 'X', 'X']
        # ['O', 'X', 'O', 'X']
        # ['X', 'O', 'X', 'O']
        # ['O', 'X', 'O', 'X']

        # [["X","O","X","X"],
        # ["O","X","X","X"],
        # ["X","X","X","O"],
        # ["O","X","O","X"]]
        
        

