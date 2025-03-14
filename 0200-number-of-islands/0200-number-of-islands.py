class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        numOfIslands = 0

        def dfs(r,c):

            if (r not in range(ROWS)
            or c not in range(COLS)
            or (r,c) in visited or
            grid[r][c]=="0"):
                return
            
            visited.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                dfs(nr,nc)

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]=="1" and (r,c) not in visited:
                    numOfIslands += 1
                    dfs(r,c)
        
        return numOfIslands
                    
