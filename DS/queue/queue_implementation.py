class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enQueue(self,item):
		self.items.insert(0,item)

	def deQueue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

if __name__ == '__main__':
	q = Queue()
	print(q.size())
	print(q.isEmpty())
	q.enQueue(1)
	q.enQueue('Two')
	print(q.items)
	print(q.deQueue())
