'''

Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using put() function and get() takes data out from the Queue.
There are various functions available in this module:

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking.
qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.


'''

from queue import LifoQueue 
  
# Initializing a stack 
stack = LifoQueue(maxsize = 3) 
  
   
# put() function to push element in the stack 
stack.put('a') 
stack.put('b') 


# qsize() show the number of elements in the stack 
print("size",stack.qsize()) 

print("Full: ", stack.full())  

print("Added new element to stack")
stack.put('c') 
  
print("Full: ", stack.full())  
  
# get() fucntion to pop element from stack in LIFO order 
print('Elements poped from the stack') 
print(stack.get()) 
print(stack.get()) 
print(stack.get()) 
  
print("Empty: ", stack.empty())