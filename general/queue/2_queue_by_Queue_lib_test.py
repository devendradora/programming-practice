'''
Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to
a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule.
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

from queue import Queue 
  
# Initializing a queue 
q = Queue(maxsize = 3)

# qsize() give the maxsize of the Queue  

# Adding of element to queue 
q.put('a') 
q.put('b') 

print("size",q.qsize())  


q.put('c') 
#q.put('d') 

# Return Boolean for Full Queue  
print("Full: ", q.full())  
  
# Removing element from queue 
print("Elements dequeued from the queue") 
print(q.get()) 
print(q.get()) 
print(q.get()) 
  
# Return Boolean for Empty Queue  
print("Empty: ", q.empty()) 
  
q.put(1) 

print("Empty: ", q.empty()) 

print("Full: ", q.full()) 

print(q.get()) 
  

