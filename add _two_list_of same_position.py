def add_numbers_list(x,y):
    i=0
    j=0
    while i<len(x) and j<len(y):
        print(x[i]+y[j])
        i+=1
        j+=1
add_numbers_list([50, 60, 10],[10, 20, 13])