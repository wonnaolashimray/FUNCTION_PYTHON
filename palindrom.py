def variable():
    i=0
    count=0
    while i< len(list1):
        if list1[i][0]==list1[i][-1]:
            count+=1
        i+=1
    print(count)
list1=['abc','xyz','aba','1221']
variable()