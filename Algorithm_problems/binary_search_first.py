def bin_search_first(A,n):
  first = 0
  last = len(A) - 1
  result = 0
  for i in range(len(A)):
    mid = (first + last) // 2
    if A[mid] == n:
      result = mid
      last = mid - 1
    elif n<A[mid]:
      last = mid - 1
    elif n>A[mid]:
      fist = mid + 1
  return result
