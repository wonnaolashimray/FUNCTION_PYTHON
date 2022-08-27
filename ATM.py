language=["english","hindi"]
def fun():
    print("please insert your ATM")
    print("Welcome to SBI")
    pin_code=int(input("enter your pin: "))
    balance=50000
    pin=1234
    if pin_code==pin:
        print("1=cash_withdrawal")
        print("2=balance_enquiry")
        print("3=deposite")
        print("4=pin_generation")
        print("5=exit")
    transaction=int(input("enter the number"))
    if transaction==1:
        withdrawal=int(input("enter the ammount"))
        if withdrawal<=balance:
            print("collect your cash",withdrawal)
            print("remaining balance",balance-withdrawal)
        else:
            print("not enough cash in your account")
    elif transaction==2:
        print("your balance",balance)
    elif transaction==3:
        deposit=int(input("enter the number"))
        print("total_ammount",balance+deposit)
    elif transaction==4:
        new_pin=int(input("enter new pin"))
        print("your new pin=",new_pin)
    elif transaction==5:
        print("Thank you for visiting")
def lan():
    user=input("enter your language: ")
    if user==language[0]:
        fun()
    else:
        print("sorry you have selected the wrong language")
lan()



# language=["english","hindi"]
# transaction=["balance_enquiry","cash withdrawl","deposit","pin_generation","quit"]
# def function():
#     pin=1234
#     balance=50000
#     user=int(input("enter the option:-"))
#     if user==1:
#         print("balance_enquiry")
#         print("enter your pin")
#         user=int(input("enter your pin"))
#         if user==pin:
#             print("your account balance=",balance)
#     elif user==2:
#         print("cash withdrawl")
#         user=int(input("enter the pin:-"))
#         if pin==user:
#             amount=int(input("enter the amount"))
#             remainder=balance-amount
#             print("remaining balance =",remainder)
#     elif user==3:
#         print("deposit")
#         amount=int(input("enter the amount"))
#         current_balance=balance+amount
#         print("new+balance = ",current_balance)
#     elif user==4:
#         print("pin_generation")
#         if pin==pin:
#             new_pin=int(input("enter the new_pin number"))
#             pin=new_pin
#             print("new_pin = ",pin,"\n","thank you for visiting SBI bank")
#     else:
#         print("quit\nthank you for visiting the SBI bank")
# def code():   
#     print("welcome to SBI world")
#     print("insert your card\ndo not remove it until the transaction is completed")
#     i=0
#     while i<len(language):
#         user1=input("enter your choice:-")
#         if user1==language[i]:
#             print("english")
#             print("sellect your option\n1.balance_enquiry\n2.cash withdrawl\n3.deposit\n4.pin_generation\n5.quit")
#             return(function())
#         else:
#             print("sorry you have selected the wrong language")
#             break
# code()