def num(x):
    sum=0
    i=0
    while i<len(x):
        sum+=x[i]
        i+=1
    print(sum)
num([1, 2, 3, 4, 5])