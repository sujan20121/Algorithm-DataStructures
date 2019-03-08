class Bin_Tree(object):

	def __init__(self,rootObj):
		self.key = rootObj
		self.lChild = None
		self.rChild = None

	def insertLeft(self,newNode):
		if self.lChild is None:
			self.lChild = Bin_Tree(newNode)
		else:
			t = Bin_Tree(newNode)
			t.lChild = self.lChild
			self.lChild = t
	def insertRight(self,newNode):
		if self.rChild is None:
			self.rChild = Bin_Tree(newNode)
		else:
			t = Bin_Tree(newNode)
			t.rChild = self.rChild
			self.rChild = t



	def get_Root(self):
		return self.key
	
	def get_lChild(self):
		return self.lChild
	
	def get_rChild(self):
		return self.rChild
	


a = Bin_Tree('B')
a.insertLeft('c1')
a.insertRight('c2')
a.lChild.insertLeft('s1')
a.lChild.insertRight('s2')
a.rChild.insertLeft('q1')
a.rChild.insertRight('q2')

#PreOrder Traversal
def PreOrder(B_T):
	#if B_T.get_Root() is not None:
	print(B_T.get_Root())
	if B_T.lChild is not None:
		PreOrder(B_T.lChild)
	if B_T.rChild is not None:
		PreOrder(B_T.rChild)

def InOrder(B_T):
	if B_T.lChild is not None:
		PreOrder(B_T.lChild)
	print(B_T.get_Root())

	if B_T.rChild is not None:
		PreOrder(B_T.rChild)

print('**********************The PreOrder************************')
PreOrder(a)

print('**********************The InOrder************************')
InOrder(a)


























