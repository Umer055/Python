s=input("Enter a string:\n")
s=s.strip()

low=0
high=len(s)-1
while low < high:
    print(low,"   ",high)
    if s[low] == s[high]:
        low+=1
        high-=1
    else:
        print("Not a Palindrome")
        break
if low >= high:
    print("It is a Palidrome")

