def check_numbers_list(x,y):
    i=0
    j=0
    while i<len(x)and i<len(y):
        if x[i]%2==0 and y[j]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i+=1
        j+=1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])