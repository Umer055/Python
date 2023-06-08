a=eval(input("Enter the integer to divide:\n"))
if a%5==0 and a%6==0:
    print("Is",a,"divisible by 5 and 6?","True")
else :
    print("Is",a,"divisible by 5 and 6?","False")

if a%5==0 or a%6==0:
    print("Is",a,"divisible by 5 or 6?","True")
else:
    print("Is",a,"divisible by 5 or 6?","False")

if (a%5==0 or a%6==0) and not (a%5==0 and a%6==0):
    print("Is",a,"divisible by 5 or 6? Or both?","True")
else:
    print("Is",a,"divisible by 5 or 6? Or not both?","False")