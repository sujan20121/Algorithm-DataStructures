#given a,b and c, calculate the value of (a^b)%c

def mod_exp(a,b,c):
 if b == 0:
  return 1
 
 elif b == 1:
  return a%c
 
 elif b%2 == 0:
  t1 = mod_exp(a,b/2,c)
  t2 = t1 ** 2
  return mod_exp(t2,1,c)
 
 else:
  t1 = a%c
  t2 = mod_exp(a,b-1,c)
  t3 = t1 *t2
  return mod_exp(t3,1,c)
