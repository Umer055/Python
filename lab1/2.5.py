x=eval(input("Enter the first value:\n"))
y=eval(input("Enter the second value:\n"))
z=eval(input("Enter the third value:\n"))
in_gratuity=eval(input("Enter the gratuity value:\n"))
list22=[x,y,z]
print("The subtotal is",list22)
total = list22[0]+list22[1]+list22[2]
gratuity=(total*in_gratuity)/100
print("subtotal of the list is",total+gratuity)