num11,num22,num33=input("Enter three numbers: \t").split(",")
num1=eval(num11)
num2=eval(num22)
num3=eval(num33)
def displaysortednumbers (num1,num2,num3):
    if num1<num2<num3 :
        return num1,num2,num3
    elif num3<num2<num1 :
        return num3,num2,num1
    elif num2<num1<num3:
        return num2,num1,num3
    elif num3<num1<num2:
        return num3,num1,num2
    elif num2<num3<num1:
        return num2,num3,num1
    elif num1<num3<num2:
        return num1,num3,num2
    
v=displaysortednumbers(num1,num2,num3)
print(v)  
