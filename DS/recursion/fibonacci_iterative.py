#find the nth term of the fibonacci series
#fibonacci series goes like 0,1,1,2,3,5,8,13,......
#this is an iterative solution for finding the nth term in the series
def fib_iter(n):
	a,b = 0,1
	for i in range(n):
		a,b = b,a+b
	return a

n = 10
print(fib_iter(10))
