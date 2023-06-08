weight_str1,price_str1=input("Enter the weight and price for package1:\n").split(",")
weight_str2,price_str2=input("Enter the weight and price for package2:\n").split(",")
price1=eval(price_str1)
price2=eval(price_str2)
weight1=eval(weight_str1)
weight2=eval(weight_str2)
unit_price1=(price1/weight1)
unit_price2=(price2/weight2)

if unit_price1<unit_price2:  
   print("Package 1 has the better price ")
elif unit_price1>unit_price2:
   print("Package 2 has the better price")
else:
   print("Both have the same price")