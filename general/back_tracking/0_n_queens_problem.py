'''

https://leetcode.com/problems/n-queens/

https://www.youtube.com/watch?v=xouin83ebxE  (Tushar Roy - Coding Made Simple)

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

'''
from typing import List

class Solution:	
	def solveNQueens(self, n: int) -> List[List[str]]:
		#T : O(n*n) exponential, S: O(n)
		rows,cols=n,n
		board=[['.']*cols for j in range(0,rows)]	
		result=[]	
		self.solve_by_backtrack(board,rows,cols,0,result)

		#print(board)				
		return result

	def solve_by_backtrack(self,board: List[List[str]], rows: int, cols: int , cur_row: int, result):
		if cur_row == rows:
			#Converting output to leetcode's output format			
			temp = [''.join(row) for row in board]
			result.append(temp)				
			return True

		for j in range(0,cols):
			if self.is_safe_position_for_queen(board,rows, cols, cur_row,j):
				board[cur_row][j]='Q'
				
				is_solved = self.solve_by_backtrack(board,rows,cols,cur_row+1,result)

				# uncomment below if you want only 1 solution
				# if is_solved:
				# 	return True
				
				# Placing queen in cur_row,j column is not safe,and does't lead to a solution
				board[cur_row][j]='.'	

		# If the queen cannot be placed in any colum for current row
		return False




	'''
	we need to check if passed row,col lies in same col or any of 2 diagonals as queen
	can move in these positions. Moreover, we need to check only upper col values, 
	upper left, upper right diagonals from current queeen position, as lower board 
	positions will be proccessed in next calls.
	Note: for 2 cells to fall in any one of diagonal,their row-col or row+col values should be same
	'''

	def is_safe_position_for_queen(self,board: List[List[str]], rows: int, cols: int, cur_row: int, cur_col: int):
		#Check if any Q present in same col for all above rows
		for i in range(cur_row):
			if board[i][cur_col] == 'Q':
				return False

		#check upper left diagonal
		for i,j in zip(range(cur_row,-1,-1),range(cur_col,-1,-1)):
			if board[i][j] == 'Q':
				return False
		
		#check upper right diagonal	
		for i,j in zip(range(cur_row,-1,-1),range(cur_col,cols))	:
			if board[i][j] == 'Q':
				return False

		return True	


sol = Solution()
print(sol.solveNQueens(4))   	
