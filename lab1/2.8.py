weight=eval(input("Enter the amount of water in kilograms:\n"))
initial=eval(input("Enter the intial Temperature:\n"))
final=eval(input("Enter the final value Temperature:\n"))
energy=weight*(final-initial)*4184
print("The energy needed is: ",energy)