class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0

        def dfs(r,c):

            if(r not in range(ROWS) or c not in range(COLS) or grid[r][c]=="0"):
                return
            
            grid[r][c]= "0"
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                dfs(nr,nc)

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    islands += 1
                    dfs(r,c)

        return islands
        