def num(x):
    i=0
    max=x[0]
    while i<len(x):
        if x[i]>max:
            max=x[i]
        i+=1
    print(max)
num([1, 2, 3, 4, 5, 6, 7, 10, -2])