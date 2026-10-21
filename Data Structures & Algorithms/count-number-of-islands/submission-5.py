class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n= len(grid)
        m=len (grid[0])
        islands=0
        def helper(i,j):
            # setting the bounds
            if i<0 or i>= n or j<0 or j>=m:
                return
            if grid[i][j]=="0":
                return
            # mark seen
            grid[i][j]="0"    
            #now lets check all for directions
            #up
            helper(i-1,j)
            #down
            helper(i+1,j)
            #right
            helper(i,j+1)
            #left   
            helper(i,j-1) 
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    islands+=1
                    helper(i,j)
        return islands