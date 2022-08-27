def num():
    user=int(input("enter the number"))
    i=1
    count=0
    while i<=user:
        if user%i==0 and user%user==0:
            count+=1
        i+=1
    if count==2:
        print("prime number")
    else:
        print("not prime number")    
num()
