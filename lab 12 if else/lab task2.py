phy=eval(input("Enter the obtained marks of phy:\n"))
chem=eval(input("Enter the obtained marks of chem:\n"))
math=eval(input("Enter the obtained marks of math:\n"))
bio=eval(input("Enter the obtained marks of bio:\n"))
computer=eval(input("Enter the obtained marks of computer:\n"))
total_marks=500
total=phy+chem+math+bio+computer
per=(total*100)/total_marks
if per>=90:
    print("You have sussessfully obtained A grade")
elif per>=80:
    print("You have sussessfully obtained B grade")
elif per>=70:    
    print("You have sussessfully obtained C grade")
elif per>=60:
    print("You have sussessfully obtained D grade")
elif per>=40:    
    print("You have sussessfully obtained E grade")
else:    
    print("You have sussessfully obtained F grade")