'''board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board () :
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {board[i][0]}|{board[i][1]}|{board[i][2]}")
        if i != 2:
            print("  -----")

def make_move(player, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid move")
        return False
    if board[row][col] != " ":
        print("That space is already occupied")
        return False
    board[row][col] = player
    return True

def has_won(player):
    # check rows
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    # check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # check diagonals
    return (player == board[0][0] == board[1][1] == board[2][2]) or (player == board[0][2] == board[1][1] == board[2][0])

def main():
    current_player = "X"
    while True:
        draw_board(),
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if make_move(current_player, row, col):
            if has_won(current_player):
                print(f"{current_player} has won!")
                break
            current_player = "O" if current_player == "X" else "X"

main()'''





 















'''def make_move(board, player, row, col):
  # Check that the chosen space is not already occupied
  if board[row][col] != '':
    return 'That space is already occupied!'
  
  # Place the player's symbol on the board
  board[row][col] = player
  return board

def check_winner(board):
  # Check rows
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != '':
      return row[0]
  
  # Check columns
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
      return board[0][col]
  
  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
    return board[0][2]
  
  # Check for a tie
  if all(all(row) for row in board):
    return 'T'
  
  # Otherwise, the game is not yet won
  return ''

def computer_turn(board, computer):
  # Choose a random space for the computer's turn
  from random import randint
  row = randint(0, 2)
  col = randint(0, 2)
  return make_move(board, computer, row, col)

board = [['', '', ''] for _ in range(3)]
computer = 'X'
player = 'O'''








'''def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
# Function to check if any player has won
def check_win(player_pos, cur_player):
 
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Function for a single game of Tic Tac Toe
def single_game(cur_player):
 
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        # Update game information
 
        # Updating grid status 
        values[move-1] = cur_player
 
        # Updating player positions
        player_pos[cur_player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
     
    # Stores the player who chooses X and O
    cur_player = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    # Stores the options
    options = ['X', 'O']
 
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1'''








            # Tic-Tac-Toe Program using
# random number in Python
 
# importing all necessary libraries
import numpy as np
import random
from time import sleep
 
# Creates an empty board
 
 
def create_board():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
 
# Check for empty places on board
 
 
def possibilities(board):
    l = []
 
    for i in range(len(board)):
        for j in range(len(board)):
 
            if board[i][j] == 0:
                l.append((i, j))
    return(l)
 
# Select a random place for the player
 
 
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return(board)
 
# Checks whether the player has three
# of their marks in a horizontal row
 
 
def row_win(board, player):
    for x in range(len(board)):
        win = True
 
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
 
        if win == True:
            return(win)
    return(win)
 
# Checks whether the player has three
# of their marks in a vertical row
 
 
def col_win(board, player):
    for x in range(len(board)):
        win = True
 
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
 
        if win == True:
            return(win)
    return(win)
 
# Checks whether the player has three
# of their marks in a diagonal row
 
 
def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win
 
# Evaluates whether there is
# a winner or a tie
 
 
def evaluate(board):
    winner = 0
 
    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
 
            winner = player
 
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
 
# Main function to start the game
 
 
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
 
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return(winner)
 
 
# Driver Code
print("Winner is: " + str(play_game()))
