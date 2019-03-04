#This is an implementation of Stack using Linked List
class Node(object):
    def __init__(self,v):
        self.val = v
        self.Next = None

class stack(object):
    def __init__(self):
        self.head = None
        
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.Next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head
            self.head = popped.Next
            return popped.val
    
    def print_head(self):
        if self.head is None:
            print('No Node!')
        else:
            print(self.head.val)
        
   

my_stack = stack()
my_stack.push(5)
my_stack.push(4)
my_stack.print_head()
my_stack.pop()
print('after pop')
my_stack.print_head()



