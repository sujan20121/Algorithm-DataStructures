#binary search exploits the sorted order of the list 
def binary_search(arr,ele):

	first = 0
	last = len(arr) - 1 #these are index variables

	found = False

	while first <= last and not found:
		mid = (first+last)//2
		if (arr[mid] == ele):
			found = True
		else:
			if (ele < arr[mid]):
				last = mid - 1
			else:
				first = mid + 1
	return found


arr = [1,2,3,4,5,6]
print(binary_search(arr,7))
