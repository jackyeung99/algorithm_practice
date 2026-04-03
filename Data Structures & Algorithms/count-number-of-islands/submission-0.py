class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        



        islands = 0

        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
        
                # BFS 
                if (i,j) not in seen and  grid[i][j] == "1":

                    q = deque([(i,j)])

                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    islands += 1 
                    print(i, j)
                    while q:
                        x,y = q.popleft()

                        for dx, dy in directions:   

                            new_x = x + dx
                            new_y = y + dy

                            if  0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in seen and grid[new_x][new_y] == "1":
                                # print(islands, new_x, new_y)
                                seen.add((new_x, new_y))
                                q.append((new_x, new_y))
                    



        return islands
