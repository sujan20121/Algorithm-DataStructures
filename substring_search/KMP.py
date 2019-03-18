def KMP_search(pattern, text):
	M = len(pattern)
	N = len(text)

	lps = [0]*M
	j = 0
	
	comp_LPS_arr(pattern,M,lps)
	
	i = 0
	while i<N:
		if pattern[j] == text[i]:
			i+=1
			j+=1
		if j ==M:
			print('found at index : ', str(i-j))
			j = lps[j-1]
		elif i<N and pattern[j] != text[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def comp_LPS_arr(pattern,M,lps):
	
	length = 0
	i = 1
	while i<M:
		if pattern[i] == pattern[length]:
			length += 1
			lps[i] = length
			i += 1

		else:
			if length != 0:
				length = lps[length - 1]
			else:
				lps[i] = 0
				i += 1


txt = 'aaabcdabcabcdabc'
pat = 'abcdabc'
#m = len(pat)
#lps = [0]*m
#comp_LPS_arr(pat,m,lps)
#print(lps)
KMP_search(pat,txt)
