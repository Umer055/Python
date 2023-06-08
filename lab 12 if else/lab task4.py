email="abc@gmail.com"
password="abcd"
email1=input("Enter the email address:\n")
password1=input("Enter the password:\n")
if email == email1 and password == password1:
    print("You are logged in")
elif email == email1 and password != password1:
    print("The password is incorrect")
elif email != email1 and password == password1:
    print("The email s incorrect")
else :
    print("Email and password both are incorrect")
