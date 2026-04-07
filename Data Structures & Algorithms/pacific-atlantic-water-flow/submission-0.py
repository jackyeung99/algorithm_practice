class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        
        n_rows = len(heights)
        n_cols = len(heights[0])

        directions = [(1,0), (-1, 0), (0,1), (0, -1)]

        def bfs(node_set):
            visited = set(node_set)
            q = deque(node_set)

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < n_rows
                        and 0 <= new_col < n_cols
                        and (new_row, new_col) not in visited
                        and heights[new_row][new_col] >= heights[row][col]
                    ):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))

            return visited


        bottom = [(n_rows - 1, col) for col in range(n_cols)]
        top = [(0, col) for col in range(n_cols)]
        left = [(row, 0) for row in range(n_rows)]
        right = [(row, n_cols - 1) for row in range(n_rows)]

        atlantic = bottom + right 
        pacific =  top + left 
        
        atlantic_nodes = bfs(atlantic)
        pacific_nodes = bfs(pacific)

        print(atlantic_nodes)

        return [ x for x in atlantic_nodes & pacific_nodes]