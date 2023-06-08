import random
cards=["Diamonds","Clubs","Spades","hearts"]
Ranks=[2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]

def the_card():
    card=random.choice(cards)
    rank=random.choice(Ranks)
    print("The card you picked is",rank,"of",card)
print(the_card())
