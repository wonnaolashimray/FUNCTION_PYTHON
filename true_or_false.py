def fun(x):
    i=0
    while i<len(x):
        if x[i]!=1:
            return False
        i+=1
    return True
print(fun([1,1,1,1]))
