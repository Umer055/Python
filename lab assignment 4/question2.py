a=eval(input("enter any number between 0 and 1000:"))
def sumdigits(a):
    num=0
    while (a>0):
        digit=a%10
        num += digit
        a//=10
    print("the number is",num)
sumdigits(a)