#Time_Complexity: O(m*n)
#Space_Complexity: O(1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lastRow = [1] * n   #Initialize lastRow with 1s till n
        
        for i in range(m-1):    #Continue till m-1
            currRow = [1] * n   #Initialize currRow with 1s till n
            for j in range(n-2, -1, -1):    #Traverse in reverse through the matrix from n-2
                currRow[j] = currRow[j+1] + lastRow[j]  #Change currRow[j] by adding with currRow[j+1] and lastRow[j]
                
            lastRow = currRow   #Change lastRow to currRow
            
            
        return lastRow[0]   #Return the first element in the lastRow