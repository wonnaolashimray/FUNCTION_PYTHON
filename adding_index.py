# def num(x):
#     i=0
#     j=1
#     sum=0
#     sum1=0
#     while i<len(x):
#         sum+=x[i]
#         sum1+=x[j]
#         j+=2
#         i+=2
#     print("sum=",sum)
#     print("sum1=",sum1)
# num([5,4,0,1,9,1])
        
l=[5,4,0,1,9]
i=0
b=[]
while i<len(l):
    d=l[i]+l[-(i+1)]
    b.append(d)
    if len(b)==2:
        break
    i=i+1
print(b)