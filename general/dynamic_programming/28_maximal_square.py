'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r=len(matrix)
        if r == 0 :return 0
        c=len(matrix[0])
        if c == 0: return 0
        
        max_sq=0
        sol_mat= [[0]*c for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                if (i == 0 or j == 0) and matrix[i][j] == '1':
                    sol_mat[i][j]=1                   
                else:
                    if matrix[i][j] == '1':
                        sol_mat[i][j]= 1 + min(sol_mat[i-1][j-1],sol_mat[i][j-1],sol_mat[i-1][j])
                
                max_sq = max(max_sq,sol_mat[i][j])
                    
        return max_sq**2            
                        
                    
                        
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

