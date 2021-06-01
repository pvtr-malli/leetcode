

class Solution:
    def find_island(self,x , y ,visited , grid):
        if not  (0 <= x < len(grid) and 0 <= y < len(grid[0])  and (x,y) not in visited and grid[x][y]):
            return 0
        visited.add((x,y))

        return (1+ self.find_island(x+1 , y , visited , grid) + self.find_island(x-1 , y , visited , grid) +
        self.find_island(x , y+1 , visited , grid) + self.find_island(x , y-1 , visited , grid))
    def maxAreaOfIsland(self, grid):
        visited = set()
        m = len(grid)
        n = len(grid[0])
        return max(self.find_island(x , y ,visited , grid) for x in range(m) for y in range(n))




print(Solution().maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
))
        
