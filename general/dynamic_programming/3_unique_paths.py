'''
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
[
	[1,2],
	[3,4],
	[5,6]
]

1->2->4->6
1->3->5->6
1->3->4->6

Output: 3

solution :
 1. For reaching any cell in first col only 1 path is possible from top left by moving vertically, so fill 1 in first col
 2. For reaching any cell in first row only 1 path is possible from top left by moving horizontally, so fill 1 in first row
 3. For all other cells , path is possible from immediate left cell and also from immediate top cell , so add these values 
 to get value of current cell


dp = [
		[1,1],
		[1,2],
		[1,3]
	]

Example 2:

Input: m = 7, n = 3
Output: 28
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9


Example 3:

[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]


1->2->3->6->9
1->2->5->6->9
1>2->5->8->9
1->4->5->6->9
1->4->5->8->9
1->4->7->8->9

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    	dp=[[0]*n for i in range(m)]

    	for i in range(0, m):
    		dp[i][0]=1

    	for j in range(0, n):
    		dp[0][j]=1

    	for i in range(1,m):
    		for j in range(1,n):
    			dp[i][j]=dp[i-1][j]	+ dp[i][j-1]

    	#print("solution matrix ",dp)		
    	return dp[m-1][n-1]	

sol = Solution()
print("Total number of unique paths from top left to bottom right ",sol.uniquePaths(3,2))      



