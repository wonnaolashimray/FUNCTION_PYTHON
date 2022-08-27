def name(x):
    i=0
    a=[]
    s=" "
    while i<len(x):
        if x[i]==" ":
            a.append(s)
            s=" "
        else:
            s+=x[i]
        i+=1
    a.append(s)
    print(a)
name("My name is wonnao")   

