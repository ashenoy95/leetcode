class Solution:
    def _getNeighbors(self, grid: List[List[int]], i: int, j: int) -> List[List[int]]:
        neighbors = []
        neighbor_positions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        
        for n_x, n_y in neighbor_positions:
            if ((i + n_x) < len(grid)) and ((j + n_y) < len(grid[0])) and ((i + n_x) >= 0) and ((j + n_y) >= 0):
                neighbors.append([i + n_x, j + n_y])
        
        return neighbors
    
    
    def _traverseGrid(self, grid: List[List[int]], visited: List[List[int]], i: int, j: int) -> int:
        if visited[i][j]:
            return 0
        
        visited[i][j] = True
        
        if grid[i][j] == 0:
            return 0
        
        area = 1
        neighbors = self._getNeighbors(grid, i, j)
        for n_x, n_y in neighbors:
            if grid[n_x][n_y] != 1:
                continue
            
            area += self._traverseGrid(grid, visited, n_x, n_y)
            
        return area
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = self._traverseGrid(grid, visited, i, j)
                maxArea = max(area, maxArea)
                
        return maxArea
