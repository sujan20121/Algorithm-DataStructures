#given a string, write a list of all the possible permutations of that string

def permute(s):
	out = []
	#base case
	if len(s) == 1:
		return [s]
	#recursion
	else:
		for i,letter in enumerate(s):
			print('letter : ', letter)
			for perm in permute(s[:i] + s[i+1:]):
				print('      perm : ', perm)
				out+=[letter+perm] 

	return out


s = 'abc'
print(permute(s))
