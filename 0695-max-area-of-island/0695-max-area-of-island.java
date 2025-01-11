class Solution {

    private static final int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};

    private int dfs(int[][] grid, int r, int c){
        if(r<0 || r>=grid.length || c<0 || c>=grid[0].length || grid[r][c]==0){
            return 0;
        }

        grid[r][c] = 0;
        int res = 1;
        for(int[] dir: directions){
            res += dfs(grid, r+dir[0], c+dir[1]);
        }
        
        return res;

    }

    public int maxAreaOfIsland(int[][] grid) {

        int ROWS = grid.length;
        int COLS = grid[0].length;
        int maxArea = 0;

        for(int r=0; r<ROWS; r++){
            for(int c=0; c<COLS; c++){
                if(grid[r][c]==1){
                    maxArea = Math.max(maxArea, dfs(grid, r, c));
                }
            }
        }

        return maxArea;
        
    }
}