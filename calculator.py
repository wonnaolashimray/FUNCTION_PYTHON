def num():
    choice=input("enter your choise :")
    user1=int(input("enter the input :"))
    user2=int(input("enter the input :"))
    if choice=="1":
        print(user1,"+",user2,"=",user1+user2)
    if choice=="2":
        print(user1,"-",user2,"=",user1-user2)
    if choice=="3":
        print(user1,"*",user2,"=",user1*user2)
    if choice=="4":
        print(user1,"/",user2,"=",user1/user2)
num()




# def function(num_x,num_y,operator):
#     if operator=="add":
#         sum=num_x+num_y
#         print(sum)
#     elif operator=="sub":
#         sub=num_x-num_y
#         print(sub)
#     elif operator=="mul":
#         mul=num_x*num_y
#         print(mul)
#     else:
#         div=num_x/num_y
#         print(div)
# function(2,3,"add")
# function(5,2,"sub")
# function(5,3,"mul")
# function(4,2,"div")