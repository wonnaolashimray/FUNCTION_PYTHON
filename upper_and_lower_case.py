def letter(x):
    i=0
    count1=0
    count2=0
    while i<len(x):
        if x[i].isupper():
            count1+=1
        if x[i].islower():
            count2+=1
        i+=1        
    print("Number of upper case=",count1) 
    print("Number of lower case=",count2)       
letter("thE QuiCK BroWn Fox")
