'''
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
For example factorial of 6 is 6*5*4*3*2*1 which is 720.
'''


class Solution:

	def factorial_iterative(self,n: int) -> int :
		prod =1
		for i in range(n,0,-1): # range 1st arg is always included , included until 2nd arg -(3rd arg default 1)
			prod = prod * i
		return prod



	def factorial_recursive(self,n: int) -> int:
		if n==0:
			return 1 # factorial of 0 is 1
		else:
			return n*self.factorial_recursive(n-1)


	def factorial_dp_top_down(self,n: int) -> int:
		f=[None]*(n+1)
		if n==0 :
			return 1
		else:
			f[n-1] = self.factorial_recursive(n-1)
		
		f[n]= n*f[n-1]
		return f[n]



	def factorial_dp_bottom_up(self,n: int) -> int:
		f=[None]*(n+1)
		f[0]=1 # factorial of 0 is 1
		for i in range(1,n+1):
			f[i] = i * f[i-1]

		return f[n]	







sol = Solution()
print(sol.factorial_iterative(6))				
print(sol.factorial_recursive(6))
print(sol.factorial_dp_top_down(6))
print(sol.factorial_dp_bottom_up(6))			