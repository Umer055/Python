import random
# Greetings
print("*************************************UMER FAROOQ*************************************")
print("***************************************WELCOME***************************************")
print("*****************************************TO******************************************")
print("*************************************TIC TAC TOE*************************************")
print("      ready for the toss")

gamerunning = True

name1 = input("Player1 enter your name :   ")
name2 = input("Player2 input your name :   ")

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}
player1 = "X"
player2 = "O"


def printboard(board):
    print(board[1], "  | ", board[2], " | ", board[3])
    print("----+-----+----")
    print(board[4], "  | ", board[5], " | ", board[6])
    print("----+-----+----")
    print(board[7], "  | ", board[8], " | ", board[9])
# printboard(board)


# Taking player input
def player_input(board, player, symbol):
    # if player == "computer":
    # decidemove()

    while True:
        inp = int(input(player + " Enter a number between 1 -9 :  "))
        if inp >= 0 and inp <= 9 and board[inp] == " ":
            board[inp] = symbol
            break
        else:
            print("It's a wrong input", player, "input it again")


def change_player(currentPlayer, symbol, player1, player2):
    # print(player)
    symbol = "O" if symbol == "X" else "X"
    currentPlayer = player2 if currentPlayer == player1 else player1
    return currentPlayer, symbol

# checking who win
# Checking along the row


def checkwin(board):
    global gamerunning
    if board[1] == board[2] == board[3] and board[1] != " ":
        if board[1] == board[2] == board[3] == "X":
            print(player1, "won")
            gamerunning = False
        else:
            print(player2, "won")
            gamerunning = False
    elif board[4] == board[5] == board[6] and board[4] != " ":
        if board[4] == board[5] == board[6] == "X":
            print(player1, "won!")
            gamerunning = False
        else:
            print(player1, "won!")
            gamerunning = False
    elif board[7] == board[8] == board[9] and board[7] != " ":
        if board[7] == board[8] == board[9] == "X":
            print(player1, "won!")
            gamerunning = False
        else:
            print(player2, "Won!")
            gamerunning = False
    elif board[1] == board[4] == board[7] and board[1] != " ":
        if board[1] == board[4] == board[7] == "X":
            print(player1, "Won!")
            gamerunning = False
        else:
            print(player2, "Won!")
            gamerunning = False
    elif board[2] == board[5] == board[8] and board[2] != " ":
        if board[2] == board[5] == board[8] == "X":
            print(player1, "Won!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif board[3] == board[6] == board[9] and board[3] != " ":
        if board[3] == board[6] == board[9] == "X":
            print(player1, "Won!!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif board[1] == board[5] == board[9] and board[1] != " ":
        if board[1] == board[5] == board[9] == "X":
            print(player1, "Won!!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif board[3] == board[5] == board[7] and board[3] != " ":
        if board[3] == board[5] == board[7] == "X":
            print(player1, "Won!!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif " " not in board.values():
        print("The game is a draw")
        gamerunning = False


def main():
    global player1
    global player2
    # toss who will go first
    import random

    while True:
        selection = input(name1 + " Select heads or tails :   ")
        coin = ["heads", "tails"]
        toss = random.choice(coin)
        if selection == toss:
            print(name1, "win the toss congratulaions the coin landed on",
                  toss, "You will go first")
            player1 = name1
            player2 = name2
            break
        elif selection not in coin:
            print(name1, "have entered a wrong input, Please input it again")
        else:
            print(name1, "lost the toss the coin landed on",
                  toss, name2, " will go first")
            player1 = name2
            player2 = name1
            break

    # choosing icon

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

    # printing the board

    currentPlayer = player1
    currentPlayerSymbol = "X"
    printboard(board)
    while gamerunning:
        player_input(board, currentPlayer, currentPlayerSymbol)
        printboard(board)
        checkwin(board)
        currentPlayer, currentPlayerSymbol = change_player(
            currentPlayer, currentPlayerSymbol, player1, player2)


main()
