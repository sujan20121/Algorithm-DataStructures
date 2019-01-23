class Stack(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)


if __name__ == '__main__':
	s = Stack()
	print(s.isEmpty())
	s.push(1)
	s.push('two')
	print(s.peek())
	s.push(True)
	print(s.size())