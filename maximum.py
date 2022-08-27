def my(num):
    i=0
    max=num[0]
    while i<len(num):
        if num[i]>max:
            max=num[i]
        i+=1
    print(max)
my([3, 5, 7, 34, 2, 89, 2, 5])
