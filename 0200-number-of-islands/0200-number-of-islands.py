class Solution:
    
    def bfs(self, r, c, grid, ROWS, COLS): 

        q = deque()
        q.append((r,c))
        directions = [[1,0], [-1,0], [0,1], [0,-1]] 
        grid[r][c] = "0"

        while q:
            r,c = q.pop()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc]=="1"):
                    grid[nr][nc] = "0"
                    q.append((nr,nc))
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    islands += 1
                    self.bfs(r,c,grid, ROWS, COLS)

        return islands
        