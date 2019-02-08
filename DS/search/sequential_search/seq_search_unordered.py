#sequential search for an element through an unordered list
def seq_search(arr,ele):
	pos = 0
	found = False

	while pos < len(arr) and not found:
		if arr[pos] == ele:
			found = True
		else:
			pos += 1

	return found


arr = [1,2,3]
ele = 3
print(seq_search(arr,ele))
