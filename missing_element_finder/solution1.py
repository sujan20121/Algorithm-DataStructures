def finder(arr1,arr2):
	arr1.sort()
	arr2.sort()

	for num1,num2 in zip(arr1,arr2):
		if num1 != num2:
			print('missing element is : ', num1)
			return
		
	print('the missing element is : ',arr1[-1])
	return
if __name__ == '__main__':
	arr1 = [1,2,3,4,5,6,7]
	arr2 = [3,4,1,6,7,2]
	finder(arr1,arr2)