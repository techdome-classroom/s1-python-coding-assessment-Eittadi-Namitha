class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
    #    write your code here        
        #return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            # Check if current cell is out of bounds or already visited or water
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                (r, c) in visited or grid[r][c] == 'W'):
                return
            # Mark current cell as visited
            visited.add((r, c))
            # Explore neighbors (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                # Start a new DFS if we find an unvisited land cell
                if grid[r][c] == 'L' and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1
        
        return island_count
