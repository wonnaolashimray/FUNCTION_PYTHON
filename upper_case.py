def my(x):
    i=0
    a=[]
    while i<len(x):
        if x[i]<="Z":
            a.append(x[i])
        i+=1
    return a
print(my("HaRugFMoP"))