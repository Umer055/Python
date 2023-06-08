x=eval(input("Enter the value of x:\n"))
y=eval(input("Enter the value of y:\n"))
if(x<=2 and y<20):
  print('The numbers x and y fall under the criteria')
  sum = x + y
  if(sum<50):
    print('The sum of x and y is:',sum)
else:
  print('The numbers x and y dont fall under the criteria')
