def c_sum(n):

	#base case
	if n == 0:
		return 0
	else:
		return n + c_sum(n-1)


print(c_sum(4))
