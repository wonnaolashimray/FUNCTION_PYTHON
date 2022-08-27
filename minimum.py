def my(num):
    i=0
    mini=num[0]
    while i<len(num):
        if num[i]<mini:
            mini=num[i]
        i+=1
    print(mini)
my([8, 6, 4, 8, 4, 50, 2, 7])



