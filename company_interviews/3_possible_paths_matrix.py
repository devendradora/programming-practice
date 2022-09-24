'''
Print all the possible paths from the top left to the bottom right of a m*n matrix. 
Constraints: 
From each cell, 
you can either move only to right or down.
The difference between the previous and next element should be equal

'''

from typing import List

class Solution:
	def printPossiblePaths(self, mat:List[List[int]]) -> None :
		paths=[]
		m,n = len(mat), len(mat[0])
		return self.possiblePathAlgo(mat,m,n,0,0,paths)

	def possiblePathAlgo(self, mat:List[List[int]],m:int,n:int,i:int,j:int,paths:List[List[int]]) -> None:
		if i == m-1 : #last row
			for right in range(i,n):
				path = mat[i][right]

		if j == n-1 : #last col
			for down in range(j,m):
				path = max[j][down]		

		self.possiblePathAlgo(mat,m,n,i+1,j, path)
		self.possiblePathAlgo(mat,m,n,i,j+1,path)		

sol = Solution()
mat = [[1, 2, 3],  
       [4, 5, 6]] 
sol.printPossiblePaths(mat)