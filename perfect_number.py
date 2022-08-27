def perfect(n):
    i=1
    while i<n:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j+=1
        if sum==i:
            print(i)
        i+=1
perfect(1000)