def fun(x):
    i=0
    s=""
    while i<len(x):
        b=str(x[i])
        s=s+b
        i+=1
    print(repr(s))
fun([53,98,71])
