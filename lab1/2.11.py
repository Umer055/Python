final=eval(input("enter the final account value="))
intrest=eval(input("enter the annual interest rate in percent="))
year=int(input("enter the number of years="))
initial=(final)/((1+(intrest/100))**year)
print("Initial deposit value is=",initial)