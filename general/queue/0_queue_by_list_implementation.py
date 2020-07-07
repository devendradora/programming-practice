		
class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, val):
		# adds val at the last 
		self.queue.append(val)

	def dequeue(self):
		# remove val at the front 
		return self.queue.pop(0)

	def front(self):
		return self.queue[0]

	def rear(self):
		return self.queue[len(self.queue)-1]	

q = Queue()

print(q.enqueue(1))   
print(q.enqueue(2))   	
print(q.enqueue(3)) 
print("printing queue",q.queue)	
print("Dequeue",q.dequeue())
print("Front",q.front())
print(q.enqueue(4)) 
print("Rear",q.rear())   	






