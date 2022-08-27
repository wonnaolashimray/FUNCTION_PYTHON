def fun(x):
    i=0
    c1=0
    c2=0
    c3=0
    c4=0
    while i<len(x):
        if x[i].isupper():
            c1+=1
        elif x[i].islower():
            c2+=1
        elif x[i].isnumeric():
            c3+=1
        else:
            c4+=1
        i+=1
        b=[c1,c2,c3,c4]
    print(b)
fun("@12,aZ45'BC!df^*")

