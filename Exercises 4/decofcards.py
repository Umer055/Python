import random
class1=["hearts","diamonds","spades","clubs"]
rank1=[1,2,3,4,5,6,7,8,9,10,"ace","jack","king","queen"]
repeat=1
while repeat==1:
    class2=random.choice(class1)
    rank2=random.choice(rank1)
    print("The card is of",class2,"and rank",rank2)
    repeat=int(input("Enter 0 to stop the program and 1 to pick a card:\n"))