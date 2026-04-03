class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        max_island = 0
        directions = [(1,0), (-1, 0), (0,1), (0, -1)]
        
        def bfs(x,y):
            q = deque([(x, y)])

            grid[x][y] = 0
            island_size = 1
            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    
                    new_x = dx + x 
                    new_y = dy + y 

                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        island_size += 1
                        q.append((new_x, new_y )) 
                        grid[new_x][new_y] = 0



            return island_size 




        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    island_size = bfs(i, j)

                    max_island = max(max_island, island_size)


        return max_island
            
        