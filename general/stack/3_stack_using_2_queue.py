"""

"""
from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        if len(self.q1) == 0:
            self.q1.append(x)
        else:
            while len(self.q1) > 0:
                self.q2.append(self.q1.popleft())
            
            self.q1.append(x)

            while len(self.q2) > 0:
                self.q1.append(self.q2.popleft())
    
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





