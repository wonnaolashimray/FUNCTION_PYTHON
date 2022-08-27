def fun(x):
    i=0
    a=0
    while i<len(x):
        if x[i]<0:
            a+=x[i]
        i+=1
    print(a)
fun([-1,2,-3,4,-5,-7,9,-10]) 