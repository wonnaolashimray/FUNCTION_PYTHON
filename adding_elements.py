def letter(x,y,z):
    a=[]
    i=x
    while i<=y:
        a.append(i)
        i+=z
    return a
print(letter(2,20,2))