def factorial(f):
    if f==1:
        return 1
    
    return f*factorial(f-1)
f=int(input("entr no: "))
var=factorial(f)
print(var)