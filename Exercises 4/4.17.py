import random
number=[0,1,2]
user=int(input("scissor (0), rock (1), paper (2):\t"))
computer=random.choice(number)
if user==computer:
    print("both have selected the same, It's a draw")
elif user==1:
    if computer==0:
        print("Computer chose Scissors, Rock smaches scissors, You Win")
    else:
        print("Computer chose Paper, Paper covers rock, You lose")
elif user==2:
    if computer==1:
        print("Computer chose Rock, Paper covers rock, You win")
    else:
        print("Computer chose Scissors, Scissors cut cut paper, You lose")
elif user==0:
    if computer==2:
        print("Computer chose paper, Scissor cut paper, You win")
    else:
        print("Computer chose Rock, Rock smaches scissor, You lose")
else:
    print("You have entered a wrong input")
