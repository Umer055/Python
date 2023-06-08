def calculator(a,b,operation):
    if operation not in ["*","+","-","/"]:
        return "Error,invalid operation is used"
    else:
        return  eval(a + operation + b)
def main():
    a=input("Enter the first number:\n")
    operation=input("Enter the operation you want to operate:\t")
    b=input("Enter the second number:\n")
    print("The answer is",calculator(a, b, operation))
main()