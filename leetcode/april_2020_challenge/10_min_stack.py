'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.


'''
from sys import maxsize 


class MinStack:

	def __init__(self):
		self.stack=[]
		self.min_val = maxsize		

	def push(self, x: int) -> None:
		if x <= self.min_val:	#If pushed x <= current min_val , Push cur min_val , change min_value to latest min val x and then push x		
			self.stack.append(self.min_val)
			self.min_val = x

		self.stack.append(x)		        

	def pop(self) -> None:
		if self.stack and self.stack.pop() == self.min_val:
			self.min_val = self.stack.pop()		

	def top(self) -> int:
		return self.stack[-1]
		

	def getMin(self) -> int:
		return self.min_val
		


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
print("After push 3 , stack  {} , min {}".format(obj.stack, obj.getMin()))

obj.push(2)
print("After Push 2, stack  {} , min {}".format(obj.stack, obj.getMin()))

obj.push(5)
print("After Push 5, stack  {} , min {}".format(obj.stack, obj.getMin()))

obj.push(1)
print("After Push 1, stack  {} , min {}".format(obj.stack, obj.getMin()))


obj.pop()
print("After Pop, stack  {} , min {}".format(obj.stack, obj.getMin()))

obj.pop()
print("After pop, stack  {} , min {}".format(obj.stack, obj.getMin()))


print("Top {}".format(obj.top()))



obj.pop()
print("After pop, stack  {} , min {}".format(obj.stack, obj.getMin()))


