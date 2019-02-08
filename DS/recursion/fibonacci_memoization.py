n = 10
cache = [None] * (n+1)

def fib_dyn(n):
	#base case
	if n == 0 or n == 1:
		return n
	#check cache
	if cache[n] != None:
		return cache[n]

	cache[n] = return fib_dyn(n-1) + fib_dyn(n-2)
	return cache[n]


print(fib_dyn(10))
