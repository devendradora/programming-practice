'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

solution:

Fill dp matrix of rows*cols by

1. first col  of all rows   : (prev row val, 0 ) + (current row val, 0)  
2. first row of all columns : (0, prev col val)  + (0, current col val)
3. other cells : min ( immediate upper cell , immeidate left cell ) + current cell

dp = [
        [1,4,5],
        [2,7,6],    
        [6,8,7]
    ]

'''

from typing import List

class Solution:
    #[[1,2,5],[3,2,1]] -> 6
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp = [[0]*cols for i in range(rows)]        
        dp[0][0] = grid[0][0]
        
        # Fill data of all rows of first column 0
        for i in range(1,rows):
            dp[i][0]= grid[i][0] + dp[i-1][0]
        
        # Fill data of all cols of first row 0
        for j in range(1,cols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
            
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j]= grid[i][j] + min(dp[i-1][j],dp[i][j-1]) 
        
        #print("Entire dp matrix ",dp)
        return dp[rows-1][cols-1]

sol = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print("path with minimum sum from top left to bottom right ",sol.minPathSum(grid))      
            
            
            
            
        
        

