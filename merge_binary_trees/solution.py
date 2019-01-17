class TreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None



	def printTree(self):
		if self.left:
			
			self.left.printTree()
		print(self.data),

		if self.right:
			
			self.right.printTree()


def mergeTrees(t1,t2):

	if t1 is None:
		return t2
	if t2 is None:
		return t1
	
	t1.data += t2.data
	
	t1.left = mergeTrees(t1.left,t2.left)
	
	t1.right = mergeTrees(t1.right,t2.right)
	return t1

	


		
if __name__ == '__main__':
	print("In main")
	tree1 = TreeNode(1)
	tree1.left = TreeNode(3)
	tree1.right = TreeNode(2)
	tree1.left.left = TreeNode(5)
	print(tree1.data)
	print(tree1.left.data)
	print(tree1.right.data)
	print(tree1.left.left.data)
	print('\n')
	
	tree2 = TreeNode(2)
	tree2.left = TreeNode(1)
	tree2.right = TreeNode(3)
	tree2.left.right = TreeNode(4)
	tree2.right.right = TreeNode(7)
	
	
	print(tree2.data)
	print(tree2.left.data)
	print(tree2.right.data)
	print(tree2.left.right.data)
	print(tree2.right.right.data)

	merged = mergeTrees(tree2,tree1)
	print('\n')
	print(merged.data)
	print(merged.left.data)
	print(merged.right.data)
	print(merged.left.left.data)
	print(merged.left.right.data)
	print(merged.right.right.data)

