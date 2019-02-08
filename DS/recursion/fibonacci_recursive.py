#find the nth term of the fibonacci series
#fibonacci series goes like 0,1,1,2,3,5,8,13,......

def fib_rec(n):
	#base case
	if n == 0 or n == 1:
		return n

	#recursion
	else:
		return fib_rec(n-1) + fib_rec(n-2)


n = 10
print(fib_rec(n))
