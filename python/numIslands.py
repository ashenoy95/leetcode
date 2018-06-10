class Solution:    
    def succ(self, v, grid):
        succ = []
        
        if v[0]+1<len(grid) and grid[v[0]+1][v[1]]=='1':
            succ.append((v[0]+1, v[1]))

        if v[0]-1>=0 and grid[v[0]-1][v[1]]=='1':
            succ.append((v[0]-1, v[1]))

        if v[1]+1<len(grid[0]) and grid[v[0]][v[1]+1]=='1':
            succ.append((v[0], v[1]+1))

        if v[1]-1>=0 and grid[v[0]][v[1]-1]=='1':
            succ.append((v[0], v[1]-1))
            
        return succ
    
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid[0])<1:
            return 0
        
        num_islands = 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=='1':
                    num_islands += 1
                    
                    q = [(i,j)]
                    while q:
                        v = q.pop()
                        visited[v[0]][v[1]] = True
                        
                        succ = self.succ(v, grid)
                        for s in succ:
                            if not visited[s[0]][s[1]]:
                                q.append(s)
                                
        return num_islands
                    
                
                
            