def values(x):
    i=0
    a=[]
    while i<len(x):
        if x[i] not in a:
            a.append(x[i])
        i+=1
    print(a,end=" ")
values([1,2,3,5,6,3,3,5,6])
