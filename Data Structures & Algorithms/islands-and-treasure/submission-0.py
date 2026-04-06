class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        


        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0), (-1, 0), (0,1), (0,-1)]

        def bfs(row, col):
            

            q = deque([[row, col, 0]])

            while q:
                x, y, level = q.popleft()

                for dx, dy in directions:
                    new_x = dx + x
                    new_y = dy + y

                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != 0 and grid[new_x][new_y] != -1 and grid[new_x][new_y] > level + 1:
                        grid[new_x][new_y] = level + 1
                        q.append([new_x, new_y, level + 1])
                        




        for row in range(rows):
            for col in range(cols): 
                if grid[row][col] == 0:
                    bfs(row, col)


        for x in grid:
            print(x)