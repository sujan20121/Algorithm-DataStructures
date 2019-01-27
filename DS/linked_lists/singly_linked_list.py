class Node(object):
	def __init__(self,val):
		self.value = val
		self.nextNode = None


if __name__ == '__main__':
	a = Node(1)
	b = Node(2)

	a.nextNode = b
	print(a.value)
	print(a.nextNode.value)
