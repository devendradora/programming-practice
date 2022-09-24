"""

"""
from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()

    def push(self, x):
        self.q1.append(x)

        for el in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())

    def pop(self):
        if len(self.q1) > 0 :
            self.q1.popleft()
        else:
            print("Empty")
    
    def top(self):
        if  len(self.q1) > 0 :
            return self.q1[0]
        else:
            print("Empty")
    
    def print_stack(self):
        print(self.q1)

s = Stack()
print(s.push(1))   
print(s.push(2))   	
print(s.push(3)) 
print(f"printing stack {s.print_stack()}")	
print("pop",s.pop())
print("top",s.top())
print(s.push(4)) 
print(f"printing stack {s.print_stack()}")





