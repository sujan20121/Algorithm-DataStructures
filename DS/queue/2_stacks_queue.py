class Queue_2_Stacks(object):
	def __init__(self):
		#initializing our 2 stacks
		self.instack = []
		self.outstack = []

	def enqueue(self,item):
		self.instack.append(item)

	def dequeue(self):
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())
		return self.outstack.pop()


if __name__ == '__main__':
	q2s = Queue_2_Stacks()
	q2s.enqueue('A')
	q2s.enqueue('B')
	print(q2s.dequeue())
	print(q2s.dequeue())



	
