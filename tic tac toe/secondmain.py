 #Greetings
print("*************************************UMER FAROOQ*************************************")
print("***************************************WELCOME***************************************")
print("*****************************************TO******************************************")
print("*************************************TIC TAC TOE*************************************")
print("     ready for the toss")

gamerunning=True
name=input("Player enter your name :   ")
# toss who will go first
import random
while True:
    selection=input("Select heads or tails :   ")
    coin=["heads","tails"]
    toss=random.choice(coin)
    if selection==toss:
        print(name,"win the toss congratulaions the coin landed on",toss,"You will go first")
        break
    elif selection not in coin:
        print(name,"have entered a wrong input, Please input it again")
    else:
        print(name,"lost the toss the coin landed on",toss,"The computer will go first")
        break
    if toss=="heads":
        currentplayer="X"
    else:
        currentplayer=="O"

# choosing icon
# player_icon="X"
# computer_icon="O"

# while True:
#     icon=input("What you want to choose X or O :   ").upper()
#     if icon == "X" or icon=="x":
#         print(name,"choose X for your icon")
#         break
#     elif icon == "O" or icon=="o":
#         print(name,"have choose O  for your icon")
#         break
#     else:
#         print(name,"have intered a wrong input, Please input it again")
# player=icon




#printing the board
board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" "}
def printboard(board):
    print(board[1],"  | ",board[2]," | ",board[3])
    print("----+-----+----")
    print(board[4],"  | ",board[5]," | ",board[6])
    print("----+-----+----")
    print(board[7],"  | ",board[8]," | ",board[9])
# printboard(board)


# Checking empty spaces
def spaceisfree(position):
    return board[position]==" "


# Taking player input
def playerinput(board,insertletter):
    run=True
    while run:
        inp=int(input("Enter a number between 1 -9 :  "))
    if inp >0 and inp<=9 and board[inp]==" " :
        if spaceisfree(inp):
            run=False
            insertletter("X",inp)
            printboard[board]=inp
    else:
        print("It's a wrong input",name,"input it again")

# Computer input
def computerinput(board):
    if board[5]==" ":
        pass


#changing player
def change_player(currentplayer):
    # print(player)
    if currentplayer == "X":
        currentplayer = "O"
    elif currentplayer == "O" :
        currentplayer = "X"
    return currentplayer


# insert the letter
def insertletter(letter,position):
    board[position]=letter





# Checking who is the winner
def checkwin(board,letter):
    return (board[1]== letter and board[2]== letter and board[3]== letter) or (board[4]== letter and board[5]== letter and board[6]== letter) or (board[7]== letter and board[8]== letter and board[9]== letter) or (board[1]== letter and board[4]== letter and board[7]== letter) or (board[2]== letter and board[5]== letter and board[8]== letter) or (board[3]== letter and board[6]== letter and board[9]== letter) or (board[1]== letter and board[5]== letter and board[9]== letter) or (board[3]== letter and board[5]== letter and board[9]== letter)


# Checking if the board is full
def boardfull(board):
    if board.count(" ") > 1:
        return True
    else:
        return False

# The main function all the code is running
def main():
    printboard(board)
    while not (boardfull(board)):
        if not (checkwin(board,"O")):
            playerinput()
            printboard()
        else:
            print("Computer wins")
            break
        if not (checkwin(board,"X")):
            inp=computerinput()
            if inp==0:
                print("The game is drawn!!!")
            else:
                insertletter("O",board)
                print("The computer places a O in position",inp," :")
                printboard()
        else:
            print("Congratulations you won!!!")
            break
while gamerunning:
    printboard(board)
    playerinput(board,insertletter)
    currentplayer =change_player(currentplayer)
    checkwin(board)
    main()