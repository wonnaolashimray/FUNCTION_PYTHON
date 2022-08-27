def num(x):
    i=1
    sum=0
    while i<=x:
        if i%3==0 or i%5==0:
            sum+=i
        i+=1
    print(sum)
num(10)