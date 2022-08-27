def my(list):
    max=list[0]
    sec=list[0]
    third=list[0]
    i=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i+=1
    i=0
    while i<len(list):
        if list[i]>sec and list[i]!=max:
            sec=list[i]
        i=i+1
    i=0
    while i<len(list):
        if list[i]>third and list[i]!=max and list[i]!=sec:
            third=list[i]
        i=i+1
    print(max)
    print(sec)
    print(third)
my(list=[10,15,20,24,30,40])