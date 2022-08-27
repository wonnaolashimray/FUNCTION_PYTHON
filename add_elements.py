def num(x):
    i=0
    sum=0
    a=[]
    while i<len(x):
        sum+=x[i]
        i+=1
    a.append(sum)
    print(x+a)
num([5,4,1])