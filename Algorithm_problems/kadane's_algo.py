def maxSubArraySum(A):
...     max_ending_here = 0
...     max_so_far = 0
...     for i in range(len(A)):
...             max_ending_here += A[i]
...             max_ending_here = max(max_ending_here,0)
...             max_so_far = max(max_ending_here,max_so_far)
...     return max_so_far
