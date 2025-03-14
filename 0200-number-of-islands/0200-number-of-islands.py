class UnionFind:

    def __init__(self, grid):
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        self.parent = []
        self.rank = []

        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    self.count += 1
                    self.parent.append(r*n+c)
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, i):
        if self.parent[i]!=i:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX!=rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootY]>self.rank[rootX]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count

class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        uf = UnionFind(grid)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    grid[r][c] = "0"
                    if r-1>=0 and grid[r-1][c]=="1":
                        uf.union(r*COLS+c, (r-1)*COLS+c)
                    if r+1<ROWS and grid[r+1][c]=="1":
                        uf.union(r*COLS+c, (r+1)*COLS+c)
                    if c-1>=0 and grid[r][c-1]=="1":
                        uf.union(r*COLS+c, r*COLS+c-1)
                    if c+1<COLS and grid[r][c+1]=="1":
                        uf.union(r*COLS+c, r*COLS+c+1)

        return uf.getCount()