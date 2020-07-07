'''
Last-In First-Out (LIFO)

'''

from collections import deque 


class Stack:
	def __init__(self):
		self.stack = deque()

	def push(self, val):
		# adds val at the last 
		self.stack.append(val)

	def pop(self):
		# remove val at the last 
		return self.stack.pop()

	def top(self):
		return self.stack[len(self.stack)-1]


s = Stack()

print(s.push(1))   
print(s.push(2))   	
print(s.push(3)) 
print("printing stack",s.stack)	
print("pop",s.pop())
print("top",s.top())
print(s.push(4)) 
print("printing stack",s.stack)	








	