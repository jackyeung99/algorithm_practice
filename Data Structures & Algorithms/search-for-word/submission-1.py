class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0,1), (0, -1)]
        
        visited = [[False] * cols for _ in range(cols)]

        def search(row, col, word_idx = 1, visited=visited):
            # print(board[row][col], word_idx)
            if word_idx == len(word):
                return True
            
            for dr, dc in directions:
                
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == word[word_idx] and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    is_found  = search(new_row, new_col, word_idx+1, visited)
                    
                    if is_found:
                        return True
                    
                    visited[new_row][new_col] = False

            return False


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited[row][col] = True
                    is_found = search(row, col, visited=visited.copy())
                    
                    if is_found:
                        return True
                    
                    visited[row][col] = False

        return False