class Node(object):

	def __init__(self,val):
		self.value = val
		self.nextNode = None

def cycle_check(node):
	#both start at the starting node
	marker1 = node
	marker2 = node

	while marker2 != None and marker2.nextNode != None:#if any one of these conditions are met, then the singly linked list is not cyclic. We're choosing marker2 because it is the faster moving node
	
		marker1 = marker1.nextNode#hops one step at a time
		marker2 = marker2.nextNode.nextNode#hops two step at a time
	
		if marker1 == marker2:#meaning marker2 has finished goind around the list once already and has caught marker1 from behind
			return True
	return False

if __name__ == '__main__':
	from nose.tools import assert_equal

	# CREATE CYCLE LIST
	a = Node(1)
	b = Node(2)
	c = Node(3)

	a.nextnode = b
	b.nextnode = c
	c.nextnode = a # Cycle Here!


	# CREATE NON CYCLE LIST
	x = Node(1)
	y = Node(2)
	z = Node(3)

	x.nextnode = y
	y.nextnode = z


	#############
	class TestCycleCheck(object):
	    
		def test(self,sol):
			assert_equal(sol(a),True)
			assert_equal(sol(x),False)
		
			print ("ALL TEST CASES PASSED")
		
	# Run Tests

	t = TestCycleCheck()
	t.test(cycle_check)




