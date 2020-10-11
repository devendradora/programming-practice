'''
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

solution:

dp = [
	  [1,1,1],
	  [1,0,1],
	  [1,1,2]
	]

'''
from typing import List

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		#T: O(MXN) , S: O(1)
		rows,cols = len(obstacleGrid),len(obstacleGrid[0])
		if obstacleGrid[0][0] == 1: #starting point has obstacle, so no paths to dest
			return 0
					
		dp=[[0]*cols for i in range(rows)]
		dp[0][0]=1

		for i in range(1, rows):
			dp[i][0]= 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
			

		for j in range(1, cols):
			dp[0][j]= 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]

		for i in range(1,rows):
			for j in range(1,cols):
				if obstacleGrid[i][j] == 1 :
					dp[i][j]=0
				else:
					dp[i][j]=dp[i-1][j]	+ dp[i][j-1]

		#print("solution matrix ",dp)		
		return dp[rows-1][cols-1]	



sol = Solution()
obstacle_grid= [
				[0,0,0],
				[0,1,0],
				[0,0,0]
			  ]

obstacle_grid =  [[1,0]] #output 0
obstacle_grid =  [[0,1,0]] #output 0
print("Total number of unique paths with obstacles from top left to bottom right",sol.uniquePathsWithObstacles(obstacle_grid))      
			



