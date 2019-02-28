def bin_search_last(A,n):
    first = 0
    last = len(A) - 1
    result = False
    for i in range(len(A)):
        mid = (first + last) // 2
        if A[mid] == n:
            result = mid
            first = mid + 1
        elif n > A[mid]:
            first = mid + 1
        elif n < A[mid]:
            last = mid - 1
    return result
