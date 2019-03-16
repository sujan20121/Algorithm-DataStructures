def strStr(haystack,needle):
	start = 0#holds the starting index in the haystack string
	while True:
		if (len(haystack) - start) < len(needle):#if reamianing portion of haystack is shorter than needle, then needle obviously does not 								exist in the haystack
			return -1

		prog = 0#holds the starting index in the needle string, goes back to zero when a mismatch occurs
	
		for i in range(start,len(haystack)):#start searching the haystack from the position pointed by start
			if haystack[i] != needle[prog]:#
				break
			else:#if letters match
				prog += 1#move the index in the needle string by 1

				if prog == len(needle):#if all the letters in the needle match, the needle is found
					return start#this value holds where the needle starts in the haystack string

		start += 1#if values don't match, start searching haystack from the next position

		if start  == len(haystack):
			return -1


h = 'mississippi'
n = 'issip'

print(strStr(h,n))
