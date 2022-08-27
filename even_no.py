def num():
    user=int(input("enter the number"))
    i=1
    a=[]
    while i<=user:
        if i%2==0:
            a.append(i)
        i+=1 
    print(a,end=" ")       
num()
