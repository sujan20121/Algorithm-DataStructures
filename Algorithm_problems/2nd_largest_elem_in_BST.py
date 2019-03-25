def find_largest(root_node):
  current = root_node
  while current:
    if not current.right:
      return current.value
    current = current.right
    
def find_2nd_largest(root_node):
  current = root_node
  while current:
    if current.right None and current.left:
      return find_largest(current.left)
      
    if current.right:
      if (current.right.right is None) and (current.right.left is None):
        return current.value
    current = current.right
    
class BST:
        def __init__(self,val):
            self.value = val
            self.left = None
            self.right = None
            
r = BST(5)
r.right = BST(8)
r.right.right = BST(12)
r.right.right.left = BST(10)
r.right.right.left.left = BST(9)
r.right.right.left.right = BST(11)

print(find_2nd_largest(r))
