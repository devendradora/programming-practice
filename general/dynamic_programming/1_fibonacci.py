'''

The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
F0,F1,F2,F3,F4,........

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

	Fn = Fn-1 + Fn-2
with seed values

   F0 = 0 and F1 = 1.

Also, Fn = {[(√5 + 1)/2] ^ n} / √5

'''
import math

class Solution:
	def fibonacci_iteration(self,n: int) -> int: 
		#Time Complexity:O(n)
		#Extra Space: O(1)
		num1 = 0
		num2 = 1
		if n < 0: 
			print("Incorrect input") 
		elif n == 0 or n == 1: 
			return n 
		else: 
			for i in range(2,n+1): 
				sum = num1 + num2
				num1 = num2
				num2 = sum 
			return num2

		

	def fibonacci_by_formula(self,n: int)-> int:
		phi = (1 + math.sqrt(5)) / 2
		return round(phi ** n / math.sqrt(5))			

	def fibonacci_recursion(self,n):
		#Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential.
		#Extra Space: O(n) if we consider the function call stack size, otherwise O(1).
		if n<0: 
			print("Incorrect input") 
		elif n==0 or n ==1: 
			return n	    
		else: 
			return self.fibonacci_recursion(n-1)+self.fibonacci_recursion(n-2)  
	

	def fibonacci_dp_top_down(self,n: int) -> int:
		f=[None]*(n+1)
		print(f)
		if n<0:
			print("Incorrect input") 
		elif n==0 or n ==1: 
			return n	    
		else: 
			f[n-1] = self.fibonacci_dp_top_down(n-1)
			f[n-2] = self.fibonacci_dp_top_down(n-2) 

		f[n]=f[n-1]+f[n-2] 
		return f[n] 


	def fibonacci_dp_bottom_up(self,n: int) -> int: 
		if n<0:
			print("Incorrect input") 			
		f=[0,1]		
		for i in range(2,n+1):
			f.append(None)
			f[i]=f[i-1]+f[i-2]
		return f[n]		         
	

sol = Solution()
print(sol.fibonacci_iteration(4))
print(sol.fibonacci_by_formula(4))															
print(sol.fibonacci_recursion(4))
print(sol.fibonacci_dp_top_down(4))	
print(sol.fibonacci_dp_bottom_up(4))

