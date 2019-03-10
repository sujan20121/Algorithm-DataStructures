A = [1,0,2,1,0,2,1,2,1]#this represents the bar plot

total = 0

for i in range(len(A)):#for each bar in the list
    lmax = 0#this holds the max height to the left
    rmax = 0#this holds the max height to the right
    
    for j in range(0,i):#for all the bars left of the current bar
        if lmax<A[j]:
            lmax = A[j]#find the max bar height
    
    for k in range(i+1,len(A)):
        if rmax < A[k]:
            rmax = A[k]
            
    t = min(lmax,rmax)
    
    if(t == 0 or A[i]>t):
        wl = 0
    else:
        wl = t - A[i]
            
     
    print('i',i)
    print('Height',A[i])
    print('lmax',lmax)
    print('rmax',rmax)
    print('wl',wl,'\n')
   
    
    total += wl


print(total)
