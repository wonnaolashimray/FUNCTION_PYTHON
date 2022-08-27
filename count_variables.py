def fun(x):
    i=0
    a=list(x)
    while i<len(a):
        j=0
        c=0
        while j<len(a):
            if a[i]==a[j]:
                c=c+1
            else:
                c=1
        print(c)
            
fun(["onring"])