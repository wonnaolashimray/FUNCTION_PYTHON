def add(f):
    if f==1:
        return 1
    else: 
        return f+add(f-1)
f=int(input("enter the number"))
var=add(f)
print(var)