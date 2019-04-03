"""
A solution to the triple steps problem from ctci.
This solution uses memoization
"""

def mainer(n):
  d = {} #this will hold pre-computed results
  return step_counter(n,d)
  
def step_counter(n,d):
  if n == 0 or n == 1:
    return 1
  elif n == 2:
    return 2
  elif n not in d:
    d[n] =  step_counter(n-3,d) + step_counter(n-2,d) + step_counter(n-1,d)
    return d[n]
    
    
print(mainer(4))#returns 7 as the possible combinations are 1,1,1,1 and 1,1,2 and 1,3 and 2,1,1 and 2,2 and 3,1
                
