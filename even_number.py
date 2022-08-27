def num():
    user=int(input("enter the number"))
    i=0
    while i<=3:
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
        i+=1
num()