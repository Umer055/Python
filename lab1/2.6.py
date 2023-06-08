num = int(input("Input a numbers:\n "))
if num<=1000 or num>=0 :
 x  = num%10 
 x1 = num//10 
 x2 = x1%10 
 x3 = x1//10 
 print("The sum of digits in the number is", x+x2+x3)
else :
 print("The entered digit is more than 1000" )
