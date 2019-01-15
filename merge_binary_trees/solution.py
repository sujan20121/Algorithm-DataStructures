class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class solution(object):
	def mergeTrees(self,t1,t2):

		if t1 and t2:
			root = TreeNode(t1.val + t2.val)
			root.left = self.mergeTrees(t1.left + t2.left)
			root.right = self.mergeTrees(t1.right + t2.right)
			return root
		else:
			return t1 or t2
		
if __name__ == '__main__':
	print("In main")
	t1 = TreeNode()
