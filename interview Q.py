list1=[10,20,30,40,10,20,40]
i=0
a=[]
b=[]
while i<len(list1):
    if list1[i] not in a:
        a.append(list1[i])
    else:
        b.append(list1[i])
    i+=1
j=0
count=0
while j<len(b):
    if b[j] in a:
        count+=1
    j+=1
print(count)



