def num(x):
    i=0
    count=0
    count1=0
    while i<len(x):
        if x[i]>=0:
            count+=1
        if x[i]<0:
            count1+=1
        i+=1
    print("positive=",count)
    print("negetive=",count1)
num([2, -7, 5, -64, -14])   
