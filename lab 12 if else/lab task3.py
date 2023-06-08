side1=eval(input("Enter the first side of the triangle:\n"))
side2=eval(input("Enter the second side of the triangle:\n"))
side3=eval(input("Enter the third side of the triangle:\n"))
if side1 == side2 == side3:
    print("The triangle is eqilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("The triangle is isosceles triangle")
else:
    print("The triangle is scalene triangle")
    