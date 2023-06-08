# Greetings
import random
print("*************************************UMER FAROOQ*************************************")
print("************************************RAVEEHA NASEEM***********************************")
print("***************************************WELCOME***************************************")
print("*****************************************TO******************************************")
print("*************************************TIC TAC TOE*************************************")
print("      ready for the toss")

repeat = "Y"
while repeat == "Y":
    gamerunning = True
    # input the names
    inp_name1 = input("Player1 enter your name :   \n -->  ").upper()
    inp_name2 = input("Player2 input your name :   \n -->  ").upper()

    # board variable
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # fuction to print the board

    def printboard(board):
        print(board[0][0], "  | ", board[0][1], " | ", board[0][2])
        print("----+-----+----")
        print(board[1][0], "  | ", board[1][1], " | ", board[1][2])
        print("----+-----+----")
        print(board[2][0], "  | ", board[2][1], " | ", board[2][2])

    # loop for the toss
    while True:
        selection = input(
            inp_name1 + " Select heads or tails :   \n -->").upper()
        coin = ["HEADS", "TAILS"]
        toss = random.choice(coin)
        if selection == toss:
            print("CONGRATULATIONS", inp_name1, "Won the toss, The coin landed on",
                  toss, "\n You will go first")
            name1 = inp_name1
            name2 = inp_name2
            break
        elif selection not in coin:
            print(inp_name1, "have entered a wrong input, Please input it again")
        else:
            print("Whoops", inp_name1, "lost the toss the coin landed on\n",
                  toss, inp_name2, " will go first")
            name1 = inp_name2
            name2 = inp_name1
            break

    # Choosing the icon
    while True:
        icon = input(" please select from 'X' or 'O' :  \n -->  ").upper()
        if icon == "X":
            print(name1, "You have choosen X for your icon")
            symbol1 = "X"
            symbol2 = "O"
            break
        elif icon == "O":
            print(name1, "You have choosen O for your icon")
            symbol1 = "O"
            symbol2 = "X"
            break
        else:
            print(inp_name1, "have entered a wrong input, Enter again!!!")

    # Taking player 1 input

    def player_input1(board):
        while True:
            inp = int(input(name1 + " Enter a number between 1 -9 :  "))
            if inp > 0 and inp < 10:
                if inp == 1 and board[0][0] == " ":
                    board[0][0] = symbol1
                    return False
                if inp == 2 and board[0][1] == " ":
                    board[0][1] = symbol1
                    return False
                if inp == 3 and board[0][2] == " ":
                    board[0][2] = symbol1
                    return False
                if inp == 4 and board[1][0] == " ":
                    board[1][0] = symbol1
                    return False
                if inp == 5 and board[1][1] == " ":
                    board[1][1] = symbol1
                    return False
                if inp == 6 and board[1][2] == " ":
                    board[1][2] = symbol1
                    return False
                if inp == 7 and board[2][0] == " ":
                    board[2][0] = symbol1
                    return False
                if inp == 8 and board[2][1] == " ":
                    board[2][1] = symbol1
                    return False
                if inp == 9 and board[2][2] == " ":
                    board[2][2] = symbol1
                    return False
            else:
                print("It's a wrong input", name1, "input it again!!!")
                return True

    # Player 2 input

    def player_input2(board):
        while True:
            inp1 = int(input(name2 + " Enter a number between 1 -9 :  "))
            if inp1 > 0 and inp1 < 10:
                if inp1 == 1 and board[0][0] == " ":
                    board[0][0] = symbol2
                    return False
                if inp1 == 2 and board[0][1] == " ":
                    board[0][1] = symbol2
                    return False
                if inp1 == 3 and board[0][2] == " ":
                    board[0][2] = symbol2
                    return False
                if inp1 == 4 and board[1][0] == " ":
                    board[1][0] = symbol2
                    return False
                if inp1 == 5 and board[1][1] == " ":
                    board[1][1] = symbol2
                    return False
                if inp1 == 6 and board[1][2] == " ":
                    board[1][2] = symbol2
                    return False
                if inp1 == 7 and board[2][0] == " ":
                    board[2][0] = symbol2
                    return False
                if inp1 == 8 and board[2][1] == " ":
                    board[2][1] = symbol2
                    return False
                if inp1 == 9 and board[2][2] == " ":
                    board[2][2] = symbol2
                    return False
            else:
                print("It's a wrong input", name2, "input it again!!!")
                return True

    # checking who win

    def checkwin(board):
        global gamerunning
        if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
            if board[0][0] == board[0][1] == board[0][2] == symbol1:
                print(name1, "won")
                gamerunning = False
            else:
                print(name2, "won")
                gamerunning = False
        elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
            if board[1][0] == board[1][1] == board[1][2] == symbol1:
                print(name1, "won!")
                gamerunning = False
            else:
                print(name1, "won!")
                gamerunning = False
        elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
            if board[2][0] == board[2][1] == board[2][1] == symbol1:
                print(name1, "won!")
                gamerunning = False
            else:
                print(name2, "Won!")
                gamerunning = False
        elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
            if board[0][0] == board[1][0] == board[2][0] == symbol1:
                print(name1, "Won!")
                gamerunning = False
            else:
                print(name2, "Won!")
                gamerunning = False
        elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
            if board[0][1] == board[1][1] == board[2][1] == symbol1:
                print(name1, "Won!")
                gamerunning = False
            else:
                print(name2, "Won!!")
                gamerunning = False
        elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
            if board[0][2] == board[1][2] == board[2][2] == symbol1:
                print(name1, "Won!!")
                gamerunning = False
            else:
                print(name2, "Won!!")
                gamerunning = False
        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            if board[0][0] == board[1][1] == board[2][2] == symbol1:
                print(name1, "Won!!")
                gamerunning = False
            else:
                print(name2, "Won!!")
                gamerunning = False
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            if board[0][2] == board[1][1] == board[2][0] == symbol1:
                print(name1, "Won!!")
                gamerunning = False
            else:
                print(name2, "Won!!")
                gamerunning = False
        elif board[0][0] in [symbol1, symbol2] and board[0][1] in [symbol1, symbol2] and board[0][2] in [symbol1, symbol2] and\
                board[1][0] in [symbol1, symbol2] and board[1][1] in [symbol1, symbol2] and board[1][2] in [symbol1, symbol2] and\
                board[2][0] in [symbol1, symbol2] and board[2][1] in [symbol1, symbol2] and board[2][2] in [symbol1, symbol2]:
            print("The game is a draw")
            gamerunning = False

    while gamerunning:
        player_input1(board)
        printboard(board)
        checkwin(board)
        if gamerunning == False:
            break
        player_input2(board)
        printboard(board)
        checkwin(board)
        if gamerunning == False:
            break

    repeat = input("Enter Y to play again and N to exit :   ").upper()
    if repeat == "N":
        print("Thnaks for playing plz give us your feedback ")
        input("Enter your feedback here :\n -->")
        print("Hope you have a good day,!!!")
    else:
        repeat == "Y"
