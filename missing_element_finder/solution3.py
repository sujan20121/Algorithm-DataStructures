#this solution has a linear time and space complexity

def finder(arr1,arr2):
	result = 0

	for num in arr1+arr2:
		result^=num
		print(result)

	print('the missing element is : ',result)
	return

if __name__ == '__main__':
	arr1 = [1,2,3,4]
	arr2 = [1,2,4]
	print(arr1+arr2)
	finder(arr1,arr2)