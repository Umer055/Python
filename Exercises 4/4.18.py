repeat=1
rate=eval(input("Enter the exchange rates from USD to RMB:\t"))

while repeat==1:
    num=int(input("Enter 0 to convert dollars to RMB and 1 vice versa:\t"))
    if num==0:
        amount=eval(input("Enter the dollar amount:\t"))
        rmb=amount*rate
        print(amount,"dollars are",rmb,"yuan")
    elif num==1:
        amount=eval(input("Enter the yuan amount:\t"))
        dollar=amount/rate
        print(amount,"yuans are",dollar,"dollars")
    else:
        print("The input number is incorrect")
    repeat=int(input("Enter 0 to stop the program and 1 to select again:\n"))
print("\n the programm ended")

