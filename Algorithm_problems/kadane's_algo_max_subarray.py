def maxSubArray(A):
  start = end = 0
  current_max = A[0]
  max_so_far = A[0]
  for i in range(1,len(A)):
    if(A[i]>A[i]+current_max and A[i]>current_max):
      current_max = A[i]
      start = i
    else:
      current_max = A[i] + current_max
      
    if(current_max > max_so_far):
      max_so_far = current_max
      end = i
   return A[start:end+i]
