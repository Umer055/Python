number=(input("Enter a number to reverse:\t"))
def reverse(number):
    print (str(number)[ : :-1])

def pallidrome(number):
    number1=eval(number)
    temp=number1
    rev=0
    while(number1>0):
        dig=number1%10
        rev=rev*10+dig
        number1=number1//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
reverse(number)
pallidrome(number)