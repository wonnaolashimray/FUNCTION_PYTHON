def num(x):
    i=0
    a=[]
    sum=0
    while i<len(x):
        sum=sum+x[i]
        a.append(sum)
        i+=1
    print(a)
num([1,2,3,4,5])