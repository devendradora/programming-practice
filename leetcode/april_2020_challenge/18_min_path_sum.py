'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

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
'''

class Solution:
    #[[1,2,5],[3,2,1]] -> 6
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp = [[0]*cols for j in range(rows)]        
        dp[0][0] = grid[0][0]
        
        print(rows)
        print(cols)
        
        for i in range(1,rows):
            dp[i][0]= grid[i][0] + dp[i-1][0]
        
        for j in range(1,cols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
            
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j]= grid[i][j] + min(dp[i-1][j],dp[i][j-1]) 
        
        return dp[rows-1][cols-1]
            
            
            
            
        
        

