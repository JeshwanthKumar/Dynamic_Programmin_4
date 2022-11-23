#Time_Complexity: O(m*n)
#Space_Complexity: O(1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)   #m is the lenght of rows in the grid
        n = len(grid[0])    #n is the length of columns in the grid
        
        for j in range(n-2, -1, -1):    #Traverse in reverse through every column from n-2 
            grid[m-1][j] += grid[m-1][j+1]  #Add the previous row same column with the previous row next column
            
        for i in range(m-2, -1, -1):    #Traverse in reverse through every row from m-2  
            grid[i][n-1] += grid[i+1][n-1]  #Add the same row previous column element with next rows previous column
        
        for i in range(m-2, -1, -1):    #For i in range with m-2 which are rows
            for j in range(n-2, -1, -1):    #For j in range with n-2 which are columns
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])   #Add the current element with minimum between grid[i+1][j] and grid[i][j+1]
                
        return grid[0][0]   #Return the first element in the grid which will give the minium path 