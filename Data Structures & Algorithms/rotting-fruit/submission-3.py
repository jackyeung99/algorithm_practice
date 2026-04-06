class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]

        q = deque([])
        # n_rotten = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append([row, col]) 
                    # n_rotten += 1

        
        max_time = 0

        while q:
            spread = False
            for _ in range(len(q)):   # process one level
                r, c = q.popleft()
                
                for dx, dy in directions:
                    
                    new_x = dx + r
                    new_y = dy + c
                    
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        spread = True
                        
                        grid[new_x][new_y] = 2
                        q.append((new_x, new_y))

            if spread:
                max_time += 1



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1 

        return max_time