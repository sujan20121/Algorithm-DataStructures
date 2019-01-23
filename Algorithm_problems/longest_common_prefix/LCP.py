def LCP(arr):
	if not arr:
		return ""

	for i in range(len(arr[0])):
		
		for string in arr[1:]:
			
			if i >=len(string) or string[i] != arr[0][i]:
				
				return arr[0][:i]
	return arr[0]


if __name__ == '__main__':
	print(LCP(["aaaaaac","aaaeee","aaarrr"]))