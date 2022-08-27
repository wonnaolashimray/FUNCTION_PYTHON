def num(x):
    user=int(input("enter the number"))
    i=0
    a=[]
    while i<len(x):
        j=0
        b=[]
        while j<len(x):
            if x[i]+x[j]==user:
                b.append(i)
                b.append(j)
            j+=1
        a.append(b)
        i+=1
    print(a)
num([1,2,3,4,5,6,7,8,9,10])