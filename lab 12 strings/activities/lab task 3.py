string1,string2=input("Enter the two strings:\n").split(",")
x=string1[0:2]
string1=string1.replace(string1[0:2],string2[0:2])
string2=string2.replace(string2[0:2],x)
print(string1,string2)