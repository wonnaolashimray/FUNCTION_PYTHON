def function(x):
    i=0
    b= []
    while i<len(x):
        if x[i] != x[i-1]:
            b.append(x[i])
        i+= 1
    print(b)
function(x=input("enter the element:"))