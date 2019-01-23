#this is linear solution, O(N) complexity. This uses hash tables
import collections

def finder(arr1,arr2):
	d = collections.defaultdict(int)


	for num in arr2:
		d[num]+=1

	for num in arr1:
		if d[num]==0:
			print('the missing element is : ', num)
			return
		else:
			d[num]-=1


if __name__ == '__main__':
	arr1 = [1,2,3,4]
	arr2 = [2,4,1]
	finder(arr1,arr2)