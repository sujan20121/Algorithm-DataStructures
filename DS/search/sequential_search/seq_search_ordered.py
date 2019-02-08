#sequential search for an element through an ordered list

def seq_search_ordered(arr,ele):
	pos = 0
	found = False
	stopped = False

	while pos < len(arr) and not found and not stopped:
		if(arr[pos] == ele):
			found = True
			
		else:
			if(arr[pos] > ele):
				stopped = True#making sure we donont search further in the list
			else:
				pos +=1
	return found


