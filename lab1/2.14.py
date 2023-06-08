x1=eval(input("Enter the x1 of side1 of the triangle:\n"))
y1=eval(input("Enter the y1 of side1 of the triangle:\n"))
x2=eval(input("Enter the x2 of side2 of the triangle:\n"))
y2=eval(input("Enter the y2 of side2 of the triangle:\n"))
x3=eval(input("Enter the x3 of side3 of the triangle:\n"))
y3=eval(input("Enter the y3 of side3 of the triangle:\n"))
side1=((x2-x1)**2+(y2-y1)**2)**0.5
side2=((x3-x2)**2+(y3-y2)**2)**0.5
side3=((x1-x3)**2+(y1-y3)**2)**0.5
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("The area of the triangle is {:2f}".format(area))