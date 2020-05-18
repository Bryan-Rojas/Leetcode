class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    self.dfs((x,y), grid)
                    count += 1
        
        return count
    
    def dfs(self, starting_point, grid):
        x, y = starting_point
        
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
            return
        
        grid[x][y] = '0'
        
        self.dfs((x+1, y), grid)
        self.dfs((x-1, y), grid)
        self.dfs((x, y+1), grid)
        self.dfs((x, y-1), grid)