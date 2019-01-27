class Node(object):
	def __init__(self,val):
		self.value = val
		self.nextNode = None

def reverse(head):
	current = head
	previous = None
	next = None
	while current:
		next_node = current.nextNode
		current.nextNode = previous
		previous = current
		current = next_node
	return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextNode = b
b.nextNode = c
c.nextNode = d

print(a.nextNode.value)
print(b.nextNode.value)
print(c.nextNode.value)

reverse(a)

print(d.nextNode.value)
print(c.nextNode.value)
print(b.nextNode.value)
		

