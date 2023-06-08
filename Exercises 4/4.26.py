num=int(input("Enter a three digit number:\t"))

temp=num
pali=0
while(num>0):
    dig=num%10
    pali=pali*10+dig
    num=num//10
if temp==pali:
    print("The number you entered is palindrome")
else:
    print("The number you entered is not a palindrome")