dollar=eval(input("Enter the amount in dollar:\n"))
penny=eval(input("Enter the amount in penny:\n"))
if dollar==1 and penny==1:
    print(dollar,"dollar","and",penny,"penny")
elif dollar!=1 and penny==1:
    print(dollar,"dollars","and",penny,"penny")
elif dollar==1 and penny!=1:
    print(dollar,"dollar","and",penny,"pennies")
else:
    print(dollar,"dollars","and",penny,"pennies")
    
