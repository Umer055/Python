import random
repeat = "Y"
while repeat == "Y":
    gamerunning = True
    # Input the names
    while True:
        inp_name1 = input("Player 1, enter your name: ").upper()
        if inp_name1.isalpha() is False:
            print("Enter letters only")
        else:
            print("Select the icon")
            break
    inp_name2 = "COMPUTER"
    # Board variable
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # Function to print the board
    def printboard(board):
        print("\t-------------------")
        print("\t |", board[0][0], " | ", board[0][1], " | ", board[0][2], "|")
        print("\t-|----|-----|----|-")
        print("\t |", board[1][0], " | ", board[1][1], " | ", board[1][2], "|")
        print("\t-|----|-----|----|-")
        print("\t |", board[2][0], " | ", board[2][1], " | ", board[2][2], "|")
        print("\t-------------------")
    symbol2 = "X"
    symbol1 = "O"
    # Function to check if a player has won
    def check_win(board, symbol):
        # Check rows
        for row in board:
            if row.count(symbol) == 3:
                return True
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == symbol:
                return True
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] == symbol:
            return True
        if board[0][2] == board[1][1] == board[2][0] == symbol:
            return True
        return False
    # Function to evaluate the board for the min-max algorithm
    def evaluate(board):
        if check_win(board, symbol2):
            return 1  # Computer wins
        elif check_win(board, symbol1):
            return -1  # Player wins
        else:
            return 0  # Tie
    # Min-max function
    def minimax(board, depth, isMaximizing):
        if check_win(board, symbol2):
            return 1  # Computer wins
        elif check_win(board, symbol1):
            return -1  # Player wins
        elif len(get_empty_cells(board)) == 0:
            return 0  # Tie
        if isMaximizing:
            bestScore = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = symbol2
                        score = minimax(board, depth + 1, False)
                        board[row][col] = " "
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = symbol1
                        score = minimax(board, depth + 1, True)
                        board[row][col] = " "
                        bestScore = min(score, bestScore)
            return bestScore
    # Function to get the empty cells on the board
    def get_empty_cells(board):
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    empty_cells.append((row, col))
        return empty_cells
    # Function to make the computer's move
    def computermove(board):
        bestScore = float('-inf')
        bestMove = None
        for move in get_empty_cells(board):
            row, col = move
            board[row][col] = symbol2
            score = minimax(board, 0, False)
            board[row][col] = " "
            if score > bestScore:
                bestScore = score
                bestMove = move
        row, col = bestMove
        board[row][col] = symbol2
    player_turn = True;
    # Main game loop
    while gamerunning:
        printboard(board)
        if player_turn:
            while True:
                row = int(input("Enter row (1, 2, or 3): ")) - 1
                col = int(input("Enter column (1, 2, or 3): ")) - 1
                if row in range(3) and col in range(3) and board[row][col] == " ":
                    board[row][col] = symbol1
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            print("Computer's turn...")
            computermove(board)

        if check_win(board, symbol1):
            print(f"{inp_name1} wins!")
            gamerunning = False
        elif check_win(board, symbol2):
            print("Computer wins!")
            gamerunning = False
        elif len(get_empty_cells(board)) == 0:
            print("It's a tie!")
            gamerunning = False
        player_turn = not player_turn
    printboard(board)
    repeat = input("Do you want to play again? (Y/N): ").upper()
