def strStr(haystack,needle):
	start = 0
	while True:
		if (len(haystack) - start) < len(needle):
			return -1

		prog = 0
	
		for i in range(start,len(haystack)):
			if haystack[i] != needle[prog]:
				break
			else:
				prog += 1
				if prog == len(needle):

					return start
		start += 1
		if start +1 == len(haystack):
			return -1


h = 'mississippi'
n = 'issip'

print(strStr(h,n))
