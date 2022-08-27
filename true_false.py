def name(x):
    i=0
    while i<len(x)-1:
        if x[i]==x[i+1]:
            return True
        i+=1
    return False          
print(name("pop"))