
# # enter your name


# toss
def toss():
    import random
    while True:
        selction=input("Choose heads or tails :  ")
        coin=["heads","tails"]
        toss=random.choice(coin)
        if selction==coin:
            print("Congratualations you have won the toss.","The coin landed on",toss)
            return True
            break
        elif selction not in coin:
            print("You have entered a wrong input. Enter again")
            return False
        else:
            print("You have lost the toss. The coin landed on",toss)
            return True
            break


# The icons for the player and the computer
player="X"
computer="O"

# Printing the board
board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" "}

def printboard(board):
    print(board[1],"  |",board[2],"  |",board[3])
    print("----+-----+----")
    print(board[4],"  |",board[5],"  |",board[6])
    print("----+-----+----")
    print(board[7],"  |",board[8],"  |",board[9])
    

def main():
    #it will print the board
    printboard(board)
    # it will be make the toss
    toss()
    #Icons are assigned 
    player="X"
    computer="O"
    
main()
    

