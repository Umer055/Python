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

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
player1 = "X"
player2 = "O"


def printboard(board):
    print(board[0][0], "  | ", board[0][1], " | ", board[0][2])
    print("----+-----+----")
    print(board[1][0], "  | ", board[1][1], " | ", board[1][2])
    print("----+-----+----")
    print(board[2][0], "  | ", board[2][1], " | ", board[2][2])
# printboard(board)


# Taking player input
def player_input1(board, player, symbol):
    while True:
        inp = int(input(name1 + " Enter a number between 1 -9 :  "))
        if inp > 0 and inp <= 9:
            if inp == "1" and board[0][0] == " ":
                board[0][0] = player1
            if inp == "2" and board[0][1] == " ":
                board[0][1] = player1
            if inp == "3" and board[0][2] == " ":
                board[0][2] = player1
            if inp == "4" and board[1][0] == " ":
                board[1][0] = player1
            if inp == "5" and board[1][1] == " ":
                board[1][1] = player1
            if inp == "6" and board[1][2] == " ":
                board[1][2] = player1
            if inp == "7" and board[2][0] == " ":
                board[2][0] = player1
            if inp == "8" and board[2][1] == " ":
                board[2][1] = player1
            if inp == "9" and board[2][2] == " ":
                board[2][2] = player1
            break
        else:
            print("It's a wrong input", name1, "input it again")


def player_input2(board, player, symbol):
    while True:
        inp = int(input(name2 + " Enter a number between 1 -9 :  "))
        if inp > 0 and inp <= 9:
            if inp == "1" and board[0][0] == " ":
                board[0][0] = player2
            if inp == "2" and board[0][1] == " ":
                board[0][1] = player2
            if inp == "3" and board[0][2] == " ":
                board[0][2] = player2
            if inp == "4" and board[1][0] == " ":
                board[1][0] = player2
            if inp == "5" and board[1][1] == " ":
                board[1][1] = player2
            if inp == "6" and board[1][2] == " ":
                board[1][2] = player2
            if inp == "7" and board[2][0] == " ":
                board[2][0] = player2
            if inp == "8" and board[2][1] == " ":
                board[2][1] = player2
            if inp == "9" and board[2][2] == " ":
                board[2][2] = player2
            break
        else:
            print("It's a wrong input", name1, "input it again")


def change_player(currentPlayer, symbol, player1, player2):
    # print(player)
    symbol = "O" if symbol == "X" else "X"
    currentPlayer = player2 if currentPlayer == player1 else player1
    return currentPlayer, symbol

# checking who win
# Checking along the row


def checkwin(board):
    global gamerunning
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
        if board[0][0] == board[0][1] == board[0][2] == "X":
            print(player1, "won")
            gamerunning = False
        else:
            print(player2, "won")
            gamerunning = False
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
        if board[1][0] == board[1][1] == board[1][2] == "X":
            print(player1, "won!")
            gamerunning = False
        else:
            print(player1, "won!")
            gamerunning = False
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
        if board[2][0] == board[2][1] == board[2][1] == "X":
            print(player1, "won!")
            gamerunning = False
        else:
            print(player2, "Won!")
            gamerunning = False
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        if board[0][0] == board[1][0] == board[2][0] == "X":
            print(player1, "Won!")
            gamerunning = False
        else:
            print(player2, "Won!")
            gamerunning = False
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        if board[0][1] == board[1][1] == board[2][1] == "X":
            print(player1, "Won!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        if board[0][2] == board[1][2] == board[2][2] == "X":
            print(player1, "Won!!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        if board[0][0] == board[1][1] == board[2][2] == "X":
            print(player1, "Won!!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        if board[0][2] == board[1][1] == board[2][0] == "X":
            print(player1, "Won!!")
            gamerunning = False
        else:
            print(player2, "Won!!")
            gamerunning = False
    elif board[0][0] in [player1, player2] and board[0][1] in [player1, player2] and board[0][2] in [player1, player2] and\
            board[1][0] in [player1, player2] and board[1][1] in [player1, player2] and board[1][2] in [player1, player2] and\
            board[2][0] in [player1, player2] and board[2][1] in [player1, player2] and board[2][2] in [player1, player2]:
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

    while True:
        icon = input("What you want to choose X or O :   ").upper()
        if icon == "X" or icon == "x":
            print(name1, "choose X for your icon")
            break
        elif icon == "O" or icon == "o":
            print(name1, "have choose O  for your icon")
            break
        else:
            print(name1, "have intered a wrong input, Please input it again")
    player1 = icon

    # printing the board

    currentPlayer = player1
    currentPlayerSymbol = "X"
    printboard(board)
    while gamerunning:
        player_input1(board, player1, icon)
        printboard(board)
        checkwin(board)
        player_input2(board, player2)
        printboard(board)

        checkwin(board)
        currentPlayer, currentPlayerSymbol = change_player(
            currentPlayer, currentPlayerSymbol, player1, player2)


main()
